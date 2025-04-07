import os
from chat2md.chat2md_core import parse_chat_json_to_markdown

def test_full_meta_output(tmp_path):
    test_file = "tests/sample_conversations.json"
    os.chdir(tmp_path)  # So output writes here

    parse_chat_json_to_markdown(test_file, full_meta=True)

    md_files = list(tmp_path.glob("*.md"))
    assert len(md_files) == 1

    content = md_files[0].read_text(encoding="utf-8")
    assert content.startswith("---")
    assert "title:" in content
    assert "conversation_id:" in content
    assert "model:" in content or "updated:" in content
    assert "<!-- msg_id:" in content

def test_no_meta_output(tmp_path):
    test_file = "tests/sample_conversations.json"
    os.chdir(tmp_path)

    parse_chat_json_to_markdown(test_file, full_meta=False)

    md_files = list(tmp_path.glob("*.md"))
    assert len(md_files) == 1

    content = md_files[0].read_text(encoding="utf-8")
    assert not content.startswith("---")
    assert "**Rick Goshen**" in content or "**ChatGPT**" in content