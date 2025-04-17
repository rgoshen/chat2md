from chat2md.services.conversation_service import process_all_conversations

def test_full_meta_output(tmp_path, sample_conversation_dict):
    # Run full-meta markdown export using in-memory fixture
    process_all_conversations(sample_conversation_dict, output_dir=tmp_path, full_meta=True)

    md_files = list(tmp_path.glob("*.md"))
    assert md_files

    content = md_files[0].read_text(encoding="utf-8")
    assert any(line.startswith("## ") for line in content.splitlines())
    assert any("[" in line and "]" in line for line in content.splitlines())
