import os
from pathlib import Path
import shutil
import tempfile
import json
from chat2md.chat2md_core import parse_chat_json_to_markdown

def test_filename_sanitization_with_real_input():
    # Copy the sample_conversations.json to a temp location
    temp_dir = tempfile.mkdtemp()
    input_file = os.path.join(temp_dir, "sample_conversations.json")
    output_dir = temp_dir

    # Copy the bundled test JSON to temp
    src_path = Path(__file__).parent / "sample_conversations.json"
    with open(src_path, "r", encoding="utf-8") as src:
        with open(input_file, "w", encoding="utf-8") as dst:
            dst.write(src.read())

    # Run the parser
    os.chdir(output_dir)
    parse_chat_json_to_markdown(input_file, full_meta=False)

    # Assert sanitized filename was created
    expected_filename = "CICD_with_GitHub_abc123-t.md"
    output_file = os.path.join(output_dir, expected_filename)

    assert os.path.exists(output_file), f"Expected file {expected_filename} not found."

    # Check that file contains expected content
    with open(output_file, "r", encoding="utf-8") as f:
        contents = f.read()
        assert "This is a test message" in contents

    # Clean up
    shutil.rmtree(temp_dir)
