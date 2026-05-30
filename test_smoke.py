"""Quick smoke test for all four fs_tools functions."""

import json
from fs_tools import read_file, list_files, search_in_file, write_file

print("=" * 50)
print("  Smoke Test: fs_tools.py")
print("=" * 50)

# test 1 - list all files
print("\n--- Test 1: list_files('resumes') ---")
r1 = list_files("resumes")
assert r1["success"], f"list_files failed: {r1['error']}"
print(f"Found {r1['total']} files:")
for f in r1["files"]:
    print(f"  - {f['name']} ({f['size_bytes']} bytes)")

# test 2 - filter by extension
print("\n--- Test 2: list_files with .pdf filter ---")
r2 = list_files("resumes", ".pdf")
assert r2["success"]
print(f"Found {r2['total']} PDF files:")
for f in r2["files"]:
    print(f"  - {f['name']}")

# test 3 - read a text file
print("\n--- Test 3: read txt file ---")
r3 = read_file("resumes/resume_arjun_sharma.txt")
assert r3["success"], f"read_file failed: {r3['error']}"
print(f"Content length: {len(r3['content'])} chars")
print(f"Metadata: {r3['metadata']}")

# test 4 - read a pdf
print("\n--- Test 4: read pdf file ---")
r4 = read_file("resumes/resume_rahul_verma.pdf")
assert r4["success"], f"read_file PDF failed: {r4['error']}"
print(f"Content length: {len(r4['content'])} chars")
print(f"First 150 chars: {r4['content'][:150]}")

# test 5 - read a docx
print("\n--- Test 5: read docx file ---")
r5 = read_file("resumes/resume_sneha_iyer.docx")
assert r5["success"], f"read_file DOCX failed: {r5['error']}"
print(f"Content length: {len(r5['content'])} chars")
print(f"First 150 chars: {r5['content'][:150]}")

# test 6 - keyword search
print("\n--- Test 6: search for 'python' ---")
r6 = search_in_file("resumes/resume_arjun_sharma.txt", "python")
assert r6["success"], f"search failed: {r6['error']}"
print(f"Found {r6['total_matches']} matches for 'python':")
for m in r6["matches"]:
    print(f"  Line {m['line_number']}: {m['line']}")

# test 7 - write a file
print("\n--- Test 7: write_file ---")
r7 = write_file("output/test_smoke.txt", "Hello from smoke test!")
assert r7["success"], f"write_file failed: {r7['error']}"
print(f"Wrote {r7['bytes_written']} bytes to {r7['filepath']}")

# test 8 - make sure errors are handled gracefully
print("\n--- Test 8: error handling ---")
r8 = read_file("this_file_doesnt_exist.xyz")
assert not r8["success"]
print(f"Got expected error: {r8['error']}")

print("\n" + "=" * 50)
print("  All tests passed!")
print("=" * 50)
