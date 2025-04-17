from chat2md.services.conversation_service import process_all_conversations

def test_filename_sanitization(tmp_path, sample_conversation_dict):
    process_all_conversations(sample_conversation_dict, output_dir=tmp_path)

    md_files = list(tmp_path.glob("*.md"))
    assert md_files

    for file in md_files:
        name = file.name
        assert " " not in name
        assert all(
            char not in name
            for char in ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
        )
