import os
import json
from pathlib import Path
from chat2md.adapters.filesystem import load_conversations_json
from chat2md.services.conversation_service import process_all_conversations

def test_standard_markdown_output(tmp_path):
    # Copy sample_conversations.json to the temp directory
    original = Path(__file__).parent / "sample_conversations.json"
    test_file = tmp_path / "sample_conversations.json"
    test_file.write_text(original.read_text(encoding="utf-8"), encoding="utf-8")

    # Load the JSON using the adapter
    data = load_conversations_json(test_file)

    # Run the full pipeline using the new service function
    process_all_conversations(data, output_dir=tmp_path)

    # Assert that one or more markdown files were generated
    md_files = list(tmp_path.glob("*.md"))
    assert md_files

    # Optional: assert content contains expected headings or speaker roles
    content = md_files[0].read_text(encoding="utf-8")
    assert "**User:**" in content or "**Assistant:**" in content
