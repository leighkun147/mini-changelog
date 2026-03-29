# mini-changelog

A small command-line changelog manager written in Python.

## Author

- Name: Leykun Hailemichael Hagos
- Student Number: 9241478125

## Project Purpose

This project stores software change notes in a plain text file named `changelog.txt`.
It is designed as a learning project for command-line argument parsing, file operations,
and structured text handling.

## Current Files in This Project

- `solution_v1.py`: Main CLI implementation.
- `test_spec.py`: Automated test suite (pytest).
- `SPEC.txt`: Assignment/specification details.
- `README.md`: This documentation.

## Data Format

Entries are saved line-by-line in `changelog.txt` using this format:

`id|date|type|description`

Example:

`1|2026-03-29|FIX|Resolved login crash`

## Supported Commands (Current Behavior)

### 1) `init`

Creates `changelog.txt` in the current directory.

- Success output: `Changelog initialized.`
- If already exists: `Error: Changelog already initialized.`

### 2) `add <type> <description>`

Appends a new entry into `changelog.txt`.

- Auto-ID starts from 1 and increments by counting existing lines.
- Date uses system date in `YYYY-MM-DD` format.
- Success output: `Entry added.`
- If file is missing: `Error: Changelog not initialized. Run 'init' first.`
- If arguments are missing: `Error: Missing arguments for 'add'.`

### 3) `list`

Not implemented yet (placeholder behavior).

- Output when initialized: `Command will be implemented in future weeks`
- If file is missing: `Error: Changelog not initialized. Run 'init' first.`

### 4) `done <id>`

Not implemented yet (placeholder behavior).

- Output when initialized with id: `Command will be implemented in future weeks`
- If file is missing: `Error: Changelog not initialized. Run 'init' first.`
- If id missing: `Error: Missing arguments for 'done'.`

### 5) `delete <id>`

Not implemented yet (placeholder behavior).

- Output when initialized with id: `Command will be implemented in future weeks`
- If file is missing: `Error: Changelog not initialized. Run 'init' first.`
- If id missing: `Error: Missing arguments for 'delete'.`

## Global Error Handling

- No command: `Error: No command provided.`
- Unknown command: `Error: Unknown command.`

## How to Run

Run commands from this project directory:

```bash
python3 solution_v1.py init
python3 solution_v1.py add FIX "Fixed bug 1"
python3 solution_v1.py list
python3 solution_v1.py done 1
python3 solution_v1.py delete 1
```

## Testing

This project uses pytest.

```bash
pytest -q
```

Latest local status: `15 passed`.

## Version Notes (V0 -> V1)

### V0 Summary

Only supported `init` and `add`. It used no loops or lists, meaning it could write data
but not display it dynamically.

### V1 Summary (planned goals)

The top of `solution_v1.py` now includes a task comment block describing these goals:

1. Implement a while loop to read `changelog.txt` and display all recorded entries.
2. Use string parsing (`split('|')`) to format output into a readable table.
3. Add a search feature to filter entries by `type` (for example, `FIX`, `FEAT`).

Note: At the moment, these V1 features are documented as tasks and are not yet fully
implemented in command behavior.

## What Was Added/Changed in This Workspace

1. Created `solution_v1.py` as the main implementation file.
2. Added a 3-task V1 comment block at the top of `solution_v1.py`.
3. Removed `solution_v0.py` so only one solution file remains.
4. Updated tests to run `solution_v1.py`.
5. Expanded this README into a detailed, all-inclusive project guide.
