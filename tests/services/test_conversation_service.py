import pytest

from chat2md.services.conversation_service import process_all_conversations


@pytest.fixture
def sample_conversations():
    """Create sample conversations data."""
    return {
        "conversations": [
            {
                "title": "Test Chat",
                "id": "test-id",
                "create_time": 1712413000.0,
                "update_time": 1712413600.0,
                "mapping": {
                    "msg1": {
                        "message": {
                            "id": "msg1",
                            "author": {"role": "user"},
                            "content": {"parts": ["Hello"]},
                            "metadata": {"model_slug": "gpt-4"}
                        }
                    }
                }
            }
        ]
    }


@pytest.fixture
def invalid_conversations():
    """Create invalid conversations data."""
    return {
        "conversations": [
            {
                "title": "Invalid Chat",
                "mapping": None  # Invalid mapping
            },
            {
                "mapping": {  # Missing title
                    "msg1": {
                        "message": {
                            "author": {"role": "user"},
                            "content": {"parts": ["Hello"]},
                            "metadata": None  # Invalid metadata
                        }
                    }
                }
            },
            {
                "title": "Invalid Messages",
                "mapping": {
                    "msg1": None,  # Invalid message
                    "msg2": {"message": None},  # Invalid message data
                    "msg3": {  # Invalid metadata structure
                        "message": {
                            "author": {"role": "user"},
                            "content": {"parts": ["Hello"]},
                            "metadata": "not a dict"
                        }
                    }
                }
            }
        ]
    }


def test_process_conversations_basic(sample_conversations, tmp_path):
    """Test basic conversation processing."""
    process_all_conversations(sample_conversations, tmp_path)
    
    output_file = tmp_path / "Test_Chat.md"
    assert output_file.exists()
    content = output_file.read_text(encoding="utf-8")
    assert "Hello" in content


def test_process_conversations_with_metadata(sample_conversations, tmp_path):
    """Test conversation processing with full metadata."""
    process_all_conversations(sample_conversations, tmp_path, full_meta=True)
    
    output_file = tmp_path / "Test_Chat.md"
    assert output_file.exists()
    content = output_file.read_text(encoding="utf-8")
    assert "title: 'Test Chat'" in content
    assert "model: 'gpt-4'" in content


def test_process_conversations_invalid_data(invalid_conversations, tmp_path):
    """Test handling of invalid conversation data."""
    process_all_conversations(invalid_conversations, tmp_path)
    
    # First conversation should be skipped (invalid mapping)
    assert not (tmp_path / "Invalid_Chat.md").exists()
    
    # Second conversation should use default title
    assert (tmp_path / "conversation-1.md").exists()
    
    # Third conversation should be processed despite invalid messages
    assert (tmp_path / "Invalid_Messages.md").exists()


def test_process_conversations_empty_data(tmp_path):
    """Test handling of empty conversations data."""
    empty_data = {"conversations": []}
    process_all_conversations(empty_data, tmp_path)
    
    # No files should be created
    assert len(list(tmp_path.glob("*.md"))) == 0


def test_process_conversations_missing_conversations(tmp_path):
    """Test handling of missing conversations key."""
    invalid_data = {}
    process_all_conversations(invalid_data, tmp_path)
    
    # No files should be created
    assert len(list(tmp_path.glob("*.md"))) == 0


def test_process_conversations_file_error(sample_conversations, tmp_path):
    """Test handling of file write errors."""
    # Make the directory read-only
    tmp_path.chmod(0o444)
    
    with pytest.raises(PermissionError):
        process_all_conversations(sample_conversations, tmp_path) 