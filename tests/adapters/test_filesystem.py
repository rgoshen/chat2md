import pytest
import json
from pathlib import Path
from chat2md.adapters.filesystem import load_conversations_json

def test_load_json_file_not_found():
    fake_path = Path("nonexistent_file.json")
    with pytest.raises(FileNotFoundError):
        load_conversations_json(fake_path)

def test_load_json_invalid_json(tmp_path):
    # Create a temp file with invalid JSON
    invalid_file = tmp_path / "invalid.json"
    invalid_file.write_text("This is not JSON", encoding="utf-8")

    with pytest.raises(json.JSONDecodeError):
        load_conversations_json(invalid_file)
