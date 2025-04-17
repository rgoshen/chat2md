import os
from pathlib import Path
from chat2md.adapters.filesystem import load_conversations_json
from chat2md.services.conversation_service import process_all_conversations

def test_full_meta_output(tmp_path):
    # Copy sample_conversations.json into the temp directory
    original = Path(__file__).parent / "sample_conversations.json"
    test_file = tmp_path / "sample_conversations.json"
    test_file.write_text(original.read_text(encoding="utf-8"), encoding="utf-8")

    # Load conversation data
    data = load_conversations_json(test_file)

    # Run full-meta markdown export
    process_all_conversations(data, output_dir=tmp_path, full_meta=True)

    # Check that at least one .md file was written
    md_files = list(tmp_path.glob("*.md"))
    assert md_files

    # Check for presence of date headings and timestamps
    content = md_files[0].read_text(encoding="utf-8")
    assert any(line.startswith("## ") for line in content.splitlines())
    assert any("[" in line and "]" in line for line in content.splitlines())  # crude timestamp
