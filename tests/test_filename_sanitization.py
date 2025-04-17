import os
import json
from pathlib import Path
from chat2md.adapters.filesystem import load_conversations_json
from chat2md.services.conversation_service import process_all_conversations

def test_filename_sanitization(tmp_path):
    # Load the original sample file
    original = Path(__file__).parent / "fixtures" / "sample_conversations.json"
    test_file = tmp_path / "sample_conversations.json"
    test_file.write_text(original.read_text(encoding="utf-8"), encoding="utf-8")

    # Load it through the adapter
    data = load_conversations_json(test_file)

    # Process all conversations into markdown
    process_all_conversations(data, output_dir=tmp_path)

    # Check that at least one .md file exists
    md_files = list(tmp_path.glob("*.md"))
    assert md_files

    # Ensure the filenames are safe (no spaces, no illegal characters)
    for file in md_files:
        name = file.name
        assert " " not in name
        assert all(
            char not in name
            for char in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
        )
