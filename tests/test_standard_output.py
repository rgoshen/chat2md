from chat2md.services.conversation_service import process_all_conversations

def test_standard_markdown_output(tmp_path, sample_conversation_dict):
    # Run the full pipeline using the in-memory fixture
    process_all_conversations(sample_conversation_dict, output_dir=tmp_path)

    # Assert that one or more markdown files were created
    md_files = list(tmp_path.glob("*.md"))
    assert md_files

    # Optional: check basic role markers exist
    content = md_files[0].read_text(encoding="utf-8")
    assert "**User:**" in content or "**Assistant:**" in content
