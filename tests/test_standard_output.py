import os
from chat2md.chat2md_core import parse_chat_json_to_markdown

def test_standard_markdown_output(tmp_path):
    # Copy sample_conversations.json into temp path
    test_file = tmp_path / "sample_conversations.json"
    with open("tests/sample_conversations.json", "r", encoding="utf-8") as f:
        test_file.write_text(f.read(), encoding="utf-8")

    # Change working directory so output is created in tmp_path
    os.chdir(tmp_path)

    # Run standard (non-full-meta) conversion
    parse_chat_json_to_markdown(test_file, full_meta=False)

    # Check output
    md_files = list(tmp_path.glob("*.md"))
    assert len(md_files) == 1

    content = md_files[0].read_text(encoding="utf-8")
    assert not content.startswith("---")  # Ensure no frontmatter
    assert "**Rick Goshen**" in content or "**ChatGPT**" in content
    assert "```python" in content  # Ensure code block was detected