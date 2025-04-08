import os
from pathlib import Path
from chat2md.chat2md_core import parse_chat_json_to_markdown

def test_full_meta_output(tmp_path):
    original = Path(__file__).parent / "sample_conversations.json"
    test_file = tmp_path / "sample_conversations.json"
    test_file.write_text(original.read_text(encoding="utf-8"), encoding="utf-8")
    os.chdir(tmp_path)

    parse_chat_json_to_markdown(test_file, full_meta=True)

    md_files = list(tmp_path.glob("*.md"))
    assert len(md_files) == 1

    content = md_files[0].read_text(encoding="utf-8")
    assert content.startswith("---")
    assert "conversation_id" in content
    assert "<!-- msg_id:" in content

def test_no_meta_output(tmp_path):
    original = Path(__file__).parent / "sample_conversations.json"
    test_file = tmp_path / "sample_conversations.json"
    test_file.write_text(original.read_text(encoding="utf-8"), encoding="utf-8")
    os.chdir(tmp_path)

    parse_chat_json_to_markdown(test_file, full_meta=False)

    md_files = list(tmp_path.glob("*.md"))
    assert len(md_files) == 1

    content = md_files[0].read_text(encoding="utf-8")
    assert not content.startswith("---")
    assert "**Rick Goshen**" in content or "**ChatGPT**" in content
    assert "```python" in content
