"""
llm_file_assistant.py - Interactive LLM assistant for resume file management

Uses Google Gemini with function calling to let users interact with
resume files using natural language. The LLM decides which tools to 
call based on what the user asks.

Setup:
    1. Set GEMINI_API_KEY env variable or put it in a .env file
    2. Run: python llm_file_assistant.py
    3. Ask things like "read all resumes" or "find python experience"
"""

import json
import os
import sys

from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
from fs_tools import TOOLS_SCHEMA, TOOL_DISPATCH


# which model to use
MODEL_NAME = "gemini-1.5-flash"

# instructions that tell the LLM how to behave
SYSTEM_INSTRUCTION = """\
You are an intelligent file assistant specialising in resume analysis.
You have access to file-system tools that let you read, list, write, and
search files. Use these tools to answer the user's questions about resume
files stored in the local file system.

Guidelines:
- When the user asks to read "all resumes", first call list_files on the
  resumes directory, then read each file individually.
- When searching for keywords, iterate over files in the directory and
  call search_in_file for each one.
- When asked to create a summary, read the resume first, then write the
  summary to the output/ directory.
- Always provide clear, well-formatted answers.
- If a tool call fails, explain the error to the user.
- The resumes directory is located at: resumes/
- The output directory for generated files is: output/
"""


def build_gemini_tools():
    """
    Convert our tool schemas into the format Gemini expects.
    Basically wrapping each tool definition in protobuf objects.
    """
    function_declarations = []

    for schema in TOOLS_SCHEMA:
        # build the parameter properties
        props = {}
        for param_name, param_info in schema["parameters"]["properties"].items():
            props[param_name] = genai.protos.Schema(
                type=genai.protos.Type.STRING,
                description=param_info.get("description", ""),
            )

        fd = genai.protos.FunctionDeclaration(
            name=schema["name"],
            description=schema["description"],
            parameters=genai.protos.Schema(
                type=genai.protos.Type.OBJECT,
                properties=props,
                required=schema["parameters"].get("required", []),
            ),
        )
        function_declarations.append(fd)

    return [genai.protos.Tool(function_declarations=function_declarations)]


def execute_tool_call(function_call):
    """Run a tool function based on what Gemini asked for."""
    func_name = function_call.name
    args = dict(function_call.args)

    func = TOOL_DISPATCH.get(func_name)
    if func is None:
        return {"success": False, "error": f"Unknown tool: {func_name}"}

    print(f"\n  🔧 Calling: {func_name}({json.dumps(args, indent=2)})")

    result = func(**args)

    # show a shortened version so the console isn't flooded
    short = truncate_result(result)
    print(f"  📋 Result: {json.dumps(short, indent=2)}")

    return result


def truncate_result(obj, max_len=200):
    """Shorten long strings for console output."""
    if isinstance(obj, dict):
        return {k: truncate_result(v, max_len) for k, v in obj.items()}
    if isinstance(obj, list):
        return [truncate_result(item, max_len) for item in obj]
    if isinstance(obj, str) and len(obj) > max_len:
        return obj[:max_len] + f"... [{len(obj)} chars total]"
    return obj


def run_assistant():
    """Main function - sets up Gemini and runs the chat loop."""

    # check for API key
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not set.")
        print("Set it with: set GEMINI_API_KEY=your-key-here")
        print("Or add it to a .env file")
        sys.exit(1)

    genai.configure(api_key=api_key)

    # set up the model with our tools
    tools = build_gemini_tools()
    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        tools=tools,
        system_instruction=SYSTEM_INSTRUCTION,
    )
    chat = model.start_chat(enable_automatic_function_calling=False)

    # welcome message
    print("=" * 60)
    print("  📁 LLM File Assistant (Gemini + Function Calling)")
    print("=" * 60)
    print()
    print("  I can help you manage and analyse resume files.")
    print("  Try queries like:")
    print('    • "Read all resumes in the resumes folder"')
    print('    • "Find resumes mentioning Python experience"')
    print('    • "Create a summary file for resume_rahul_verma.pdf"')
    print()
    print("  Type 'quit' or 'exit' to leave.")
    print("-" * 60)

    # main loop
    while True:
        try:
            user_input = input("\n🧑 You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nGoodbye! 👋")
            break

        if not user_input:
            continue
        if user_input.lower() in ("quit", "exit", "q"):
            print("\nGoodbye! 👋")
            break

        try:
            response = chat.send_message(user_input)

            # the model might want to call tools multiple times
            # so we loop until it gives us a text response
            while response.candidates[0].content.parts:
                # check if there are any function calls
                function_calls = [
                    part.function_call
                    for part in response.candidates[0].content.parts
                    if part.function_call.name
                ]

                if not function_calls:
                    break  # no more tool calls, model is done

                # execute each tool call and collect results
                tool_responses = []
                for fc in function_calls:
                    result = execute_tool_call(fc)
                    tool_responses.append(
                        genai.protos.Part(
                            function_response=genai.protos.FunctionResponse(
                                name=fc.name,
                                response={"result": json.dumps(result)},
                            )
                        )
                    )

                # send results back to the model
                response = chat.send_message(
                    genai.protos.Content(parts=tool_responses)
                )

            # print the final text answer
            text_parts = [
                part.text
                for part in response.candidates[0].content.parts
                if part.text
            ]
            if text_parts:
                print(f"\n🤖 Assistant: {''.join(text_parts)}")
            else:
                print("\n🤖 Assistant: (No response generated)")

        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("   Try again or rephrase your query.")


if __name__ == "__main__":
    run_assistant()
