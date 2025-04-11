import os
from pathlib import Path
    # Run the actual chat2md conversion on the sample input
from chat2md.chat2md_core import parse_chat_json_to_markdown

# Test full-meta mode: ensures YAML frontmatter and extended metadata are included
def test_full_meta_output(tmp_path):
    # Load the bundled sample_conversations.json
    original = Path(__file__).parent / "sample_conversations.json"
    # Copy test file into temp path to isolate output
    test_file = tmp_path / "sample_conversations.json"
    test_file.write_text(original.read_text(encoding="utf-8"), encoding="utf-8")
    # Set working directory so output Markdown is generated here
    os.chdir(tmp_path)

    # Run the actual chat2md conversion on the sample input
    parse_chat_json_to_markdown(test_file, full_meta=True)

    # Collect generated Markdown files in the temp directory
    md_files = list(tmp_path.glob("*.md"))
    # Assert the expected number of output files were created (now 2 due to added test)
    assert len(md_files) == 2

    content = md_files[0].read_text(encoding="utf-8")
    assert content.startswith("---")
    assert "conversation_id" in content
    assert "<!-- msg_id:" in content

# Test standard mode (no meta): ensures minimal markdown output without frontmatter
def test_no_meta_output(tmp_path):
    # Load the bundled sample_conversations.json
    original = Path(__file__).parent / "sample_conversations.json"
    # Copy test file into temp path to isolate output
    test_file = tmp_path / "sample_conversations.json"
    test_file.write_text(original.read_text(encoding="utf-8"), encoding="utf-8")
    # Set working directory so output Markdown is generated here
    os.chdir(tmp_path)

    # Run the actual chat2md conversion on the sample input
    parse_chat_json_to_markdown(test_file, full_meta=False)

    # Collect generated Markdown files in the temp directory
    md_files = list(tmp_path.glob("*.md"))
    # Assert the expected number of output files were created (now 2 due to added test)
    assert len(md_files) == 2

    content = md_files[0].read_text(encoding="utf-8")
    assert not content.startswith("---")
    assert "**Rick Goshen**" in content or "**ChatGPT**" in content
    assert "```python" in content
