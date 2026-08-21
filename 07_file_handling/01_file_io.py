"""
FILE HANDLING — Python vs Node's `fs` module

Node (async, callback/promise-based):
    const fs = require('fs');
    fs.writeFileSync('data.txt', 'Hello World');
    const content = fs.readFileSync('data.txt', 'utf-8');

Python (sync by default, uses `with` for auto-cleanup):
"""

# --- Writing to a file ---
# `with` = context manager, AUTO-CLOSES the file even if an error happens.
# JS has no direct equivalent — you'd use try/finally to guarantee fs.close()
with open("data.txt", "w") as f:      # "w" = write mode (overwrites existing file)
    f.write("Hello World\n")
    f.write("Second line\n")

# --- Reading a file ---
with open("data.txt", "r") as f:      # "r" = read mode (default)
    content = f.read()
    print(content)

# --- Reading line by line (memory efficient for big files) ---
with open("data.txt", "r") as f:
    for line in f:                     # iterating a file object gives you lines, one at a time
        print("Line:", line.strip())    # .strip() removes trailing \n

# --- Appending to a file ---
with open("data.txt", "a") as f:      # "a" = append mode
    f.write("Third line (appended)\n")

# --- Reading all lines into a list ---
with open("data.txt", "r") as f:
    lines = f.readlines()             # JS: fs.readFileSync(...).toString().split('\n')
    print(lines)

# --- Working with JSON (like JSON.parse / JSON.stringify in JS) ---
import json

data = {"name": "Rahul", "skills": ["Python", "JS", "AI"]}

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)      # JS: fs.writeFileSync('data.json', JSON.stringify(data, null, 2))

with open("data.json", "r") as f:
    loaded = json.load(f)              # JS: JSON.parse(fs.readFileSync('data.json'))
    print(loaded)

# JSON string <-> Python object (without a file) — same as JS JSON.stringify/parse
json_string = json.dumps(data)          # object -> string
print(json_string)
back_to_dict = json.loads(json_string)   # string -> object
print(back_to_dict)

# cleanup demo files
import os
os.remove("data.txt")
os.remove("data.json")

# TODO (practice): write a function that reads a CSV-like text file
# (comma separated) and returns a list of dicts, one per row.
