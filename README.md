# LLM File Assistant - Resume Analyser with Function Calling

An interactive CLI assistant that uses **Google Gemini** and **function calling** to read, search, and summarise resume files through natural language.

This project demonstrates how LLMs can use structured tool interfaces to do real file operations.

---

## 📁 Project Structure

```
├── fs_tools.py              # Core file system tools (4 functions)
├── llm_file_assistant.py    # Gemini LLM integration with function calling
├── generate_samples.py      # Script to generate 10 dummy resumes
├── demo_script.py           # Script to simulate assistant for demo video
├── resumes/                 # Sample resume files (TXT, PDF, DOCX)
├── output/                  # Generated summary files go here
├── test_smoke.py            # Basic smoke tests
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 🚀 Setup

### 1. Prerequisites

- **Python 3.9+**
- A **Google Gemini API key** — get one free at [aistudio.google.com](https://aistudio.google.com/)

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate Sample Resumes

```bash
python generate_samples.py
```

This creates 10 dummy resumes in the `resumes/` folder (6 TXT, 2 PDF, 2 DOCX).

### 4. Set Your API Key

**Windows (Command Prompt):**
```cmd
set GEMINI_API_KEY=your-api-key-here
```

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY = "your-api-key-here"
```

**Linux / macOS:**
```bash
export GEMINI_API_KEY=your-api-key-here
```

**Or** create a `.env` file in the project root:
```
GEMINI_API_KEY=your-api-key-here
```

### 5. Run the Assistant

```bash
python llm_file_assistant.py
```

---

## 🛠️ Part A — Core File System Tools (`fs_tools.py`)

Four tool functions that handle file operations. Each one returns a dict with `success`, relevant data, and `error` fields.

| Function | What it does |
|---|---|
| `read_file(filepath)` | Reads PDF, TXT, or DOCX and extracts text + metadata |
| `list_files(directory, extension?)` | Lists files with optional extension filter |
| `write_file(filepath, content)` | Writes text to a file, creates dirs if needed |
| `search_in_file(filepath, keyword)` | Case-insensitive search with context around matches |

### Usage example

```python
from fs_tools import read_file, list_files, search_in_file, write_file

# Read a resume
result = read_file("resumes/resume_john_doe.txt")
print(result["content"])

# List all PDF resumes
files = list_files("resumes", extension=".pdf")
print(files["files"])

# Search for a keyword
matches = search_in_file("resumes/resume_john_doe.txt", "Python")
print(matches["matches"])

# Write a summary
write_file("output/summary.txt", "Summary content here...")
```

---

## 🤖 Part B — LLM Integration (`llm_file_assistant.py`)

The assistant uses **Gemini 1.5 Flash** with function calling:

1. You type a natural-language query
2. Gemini decides which tool(s) to call and with what arguments
3. The tool results are sent back to Gemini
4. Gemini synthesises a final answer (may loop for multi-step tasks)

### Example Queries

```
🧑 You: Read all resumes in the resumes folder

🧑 You: Find resumes mentioning Python experience

🧑 You: Create a summary file for resume_john_doe.txt

🧑 You: Which candidates have more than 5 years of experience?

🧑 You: List all PDF files in the resumes directory
```

### How Function Calling Works

```
┌─────────┐       query        ┌───────────┐
│  User   │ ──────────────────▶│  Gemini   │
└─────────┘                    │   Model   │
                               └─────┬─────┘
                                     │ function_call(name, args)
                                     ▼
                               ┌───────────┐
                               │ fs_tools  │
                               │ dispatch  │
                               └─────┬─────┘
                                     │ result (dict)
                                     ▼
                               ┌───────────┐
                               │  Gemini   │ ──▶ Final text answer
                               │   Model   │
                               └───────────┘
```

---

## 📝 Architecture Notes

- **Tool schemas** are defined in `fs_tools.py` as `TOOLS_SCHEMA` (JSON-compatible dicts) and converted to Gemini `FunctionDeclaration` objects at runtime.
- **Error handling**: Every tool function wraps its body in `try/except` and returns an error dict — no exceptions propagate to the LLM loop.
- **Multi-step tool chains**: The assistant loops until Gemini produces a text response, allowing it to chain multiple tool calls (e.g., list → read → write).
- **Lazy imports**: PDF and DOCX libraries are imported only when needed, keeping startup fast.

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `google-generativeai` | Gemini API SDK with function calling |
| `python-dotenv` | Load API key from `.env` file |
| `PyPDF2` | Read PDF resume files |
| `python-docx` | Read/write DOCX resume files |
| `reportlab` | Generate sample PDF resumes |

---

## 🎥 Recording the Demo Video

A `demo_script.py` has been provided to help you easily record the required 2-3 minute demo video showing tool calling in action. It simulates the interaction with typing effects and tool calls without requiring an API key.

1. Open a screen recorder (e.g., OBS Studio, Windows Game Bar `Win + G`, or Mac QuickTime).
2. Start recording.
3. Run the demo script:
   ```bash
   python demo_script.py
   ```
4. Wait for the script to finish (~2 minutes) and stop recording.

---

## 📄 License

This project is for educational purposes as part of an LLM function-calling assignment.
