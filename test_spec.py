# Öğrenci Numarası: 9241478125
import subprocess
import os
import pytest
import datetime

def run_cmd(args):
    """Helper to run the solution script and capture output."""
    process = subprocess.Popen(
        ["python3", "solution_v0.py"] + args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate()
    return stdout.strip()

@pytest.fixture(autouse=True)
def cleanup():
    """Ensure changelog.txt is removed before and after each test."""
    if os.path.exists("changelog.txt"):
        os.remove("changelog.txt")
    yield
    if os.path.exists("changelog.txt"):
        os.remove("changelog.txt")

def test_1_no_command_error():
    # 1. Error when no command is provided
    assert run_cmd([]) == "Error: No command provided."

def test_2_unknown_command_error():
    # 2. Error when an unknown command is provided
    assert run_cmd(["unknown"]) == "Error: Unknown command."

def test_3_init_success():
    # 3. Successful initialization
    assert run_cmd(["init"]) == "Changelog initialized."
    assert os.path.exists("changelog.txt")

def test_4_init_already_initialized_error():
    # 4. Error when initializing an already existing changelog
    run_cmd(["init"])
    assert run_cmd(["init"]) == "Error: Changelog already initialized."

def test_5_add_without_init_error():
    # 5. Error when trying to add an entry before initialization
    assert run_cmd(["add", "FEAT", "Initial commit"]) == "Error: Changelog not initialized. Run 'init' first."

def test_6_add_success_first_entry():
    # 6. Successful addition of the first entry
    run_cmd(["init"])
    assert run_cmd(["add", "FIX", "Fixed bug 1"]) == "Entry added."
    with open("changelog.txt", "r") as f:
        content = f.read()
        date_str = str(datetime.date.today())
        expected = "1|" + date_str + "|FIX|Fixed bug 1\n"
        assert content == expected

def test_7_add_success_multiple_entries_and_unique_id():
    # 7. Successful addition of multiple entries with unique IDs
    run_cmd(["init"])
    run_cmd(["add", "FEAT", "First feature"])
    run_cmd(["add", "DOCS", "Added readme"])
    
    with open("changelog.txt", "r") as f:
        lines = f.readlines()
        assert lines[0].startswith("1|")
        assert "|FEAT|First feature" in lines[0]
        assert lines[1].startswith("2|")
        assert "|DOCS|Added readme" in lines[1]

def test_8_add_missing_both_args_error():
    # 8. Error when 'add' is called without any arguments
    run_cmd(["init"])
    assert run_cmd(["add"]) == "Error: Missing arguments for 'add'."

def test_9_add_missing_one_arg_error():
    # 9. Error when 'add' is called with only one argument
    run_cmd(["init"])
    assert run_cmd(["add", "FIX"]) == "Error: Missing arguments for 'add'."

def test_10_list_future_implementation():
    # 10. Message for future implementation of 'list'
    assert run_cmd(["list"]) == "Command will be implemented in future weeks"

def test_11_search_future_implementation():
    # 11. Message for future implementation of 'search'
    assert run_cmd(["search"]) == "Command will be implemented in future weeks"
