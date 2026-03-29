# Öğrenci Numarası: 9241478125
import subprocess
import os
import pytest
import datetime

def run_cmd(args):
    """Helper to run the solution script and capture output."""
    process = subprocess.Popen(
        ["python3", "solution_v1.py"] + args,
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

# --- GENERAL ERRORS ---
def test_1_no_command_error():
    assert run_cmd([]) == "Error: No command provided."

def test_2_unknown_command_error():
    assert run_cmd(["unknown"]) == "Error: Unknown command."

# --- INIT TESTS ---
def test_3_init_success():
    assert run_cmd(["init"]) == "Changelog initialized."
    assert os.path.exists("changelog.txt")

def test_4_init_already_initialized_error():
    run_cmd(["init"])
    assert run_cmd(["init"]) == "Error: Changelog already initialized."

# --- ADD TESTS ---
def test_5_add_without_init_error():
    assert run_cmd(["add", "FEAT", "Initial commit"]) == "Error: Changelog not initialized. Run 'init' first."

def test_6_add_missing_args_error():
    run_cmd(["init"])
    assert run_cmd(["add"]) == "Error: Missing arguments for 'add'."
    assert run_cmd(["add", "FIX"]) == "Error: Missing arguments for 'add'."

def test_7_add_success():
    run_cmd(["init"])
    assert run_cmd(["add", "FIX", "Fixed bug 1"]) == "Entry added."
    with open("changelog.txt", "r") as f:
        content = f.read()
        date_str = str(datetime.date.today())
        expected = "1|" + date_str + "|FIX|Fixed bug 1\n"
        assert content == expected

# --- LIST TESTS ---
def test_8_list_without_init_error():
    assert run_cmd(["list"]) == "Error: Changelog not initialized. Run 'init' first."

def test_9_list_success_future_msg():
    run_cmd(["init"])
    assert run_cmd(["list"]) == "Command will be implemented in future weeks"

# --- DONE TESTS ---
def test_10_done_without_init_error():
    assert run_cmd(["done", "1"]) == "Error: Changelog not initialized. Run 'init' first."

def test_11_done_missing_args_error():
    run_cmd(["init"])
    assert run_cmd(["done"]) == "Error: Missing arguments for 'done'."

def test_12_done_success_future_msg():
    run_cmd(["init"])
    assert run_cmd(["done", "1"]) == "Command will be implemented in future weeks"

# --- DELETE TESTS ---
def test_13_delete_without_init_error():
    assert run_cmd(["delete", "1"]) == "Error: Changelog not initialized. Run 'init' first."

def test_14_delete_missing_args_error():
    run_cmd(["init"])
    assert run_cmd(["delete"]) == "Error: Missing arguments for 'delete'."

def test_15_delete_success_future_msg():
    run_cmd(["init"])
    assert run_cmd(["delete", "1"]) == "Task #1 not found"

def test_16_delete_existing_entry_success():
    run_cmd(["init"])
    run_cmd(["add", "FIX", "Fixed bug 1"])
    assert run_cmd(["delete", "1"]) == "Deleted task #1"
    with open("changelog.txt", "r") as f:
        assert f.read() == ""

if __name__ == "__main__":
    pytest.main([__file__])
