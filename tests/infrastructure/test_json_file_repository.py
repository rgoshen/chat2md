import json
import pytest
from datetime import datetime
from pathlib import Path  # noqa: F401 - used via tmp_path fixture

from chat2md.domain.entities.conversation import Conversation
from chat2md.infrastructure.persistence.json_file_repository import JsonFileRepository


@pytest.fixture
def repository():
    """Create a JsonFileRepository instance."""
    return JsonFileRepository()


def test_load_conversations_basic(repository, tmp_path):
    """Test loading basic conversation structure."""
    # Create a simple test JSON file
    json_data = {
        "conversations": [{
            "title": "Test Chat",
            "id": "test-id",
            "create_time": 1712413000.0,
            "update_time": 1712413600.0,
            "mapping": {
                "msg1": {
                    "message": {
                        "id": "msg1",
                        "author": {"role": "user"},
                        "create_time": 1712413260.0,
                        "content": {"parts": ["Hello"]},
                        "metadata": {"model_slug": "gpt-4"}
                    }
                }
            }
        }]
    }
    
    json_file = tmp_path / "test.json"
    json_file.write_text(json.dumps(json_data))
    
    conversations = repository.load_conversations(json_file)
    assert len(conversations) == 1
    
    conv = conversations[0]
    assert conv.title == "Test Chat"
    assert conv.id == "test-id"
    assert conv.create_time == datetime.fromtimestamp(1712413000.0)
    assert conv.update_time == datetime.fromtimestamp(1712413600.0)
    assert conv.model == "gpt-4"
    
    assert len(conv.messages) == 1
    msg = conv.messages[0]
    assert msg.author == "user"
    assert msg.content == "Hello"
    assert msg.create_time == datetime.fromtimestamp(1712413260.0)
    assert msg.message_id == "msg1"


def test_load_conversations_empty_mapping(repository, tmp_path):
    """Test handling of conversations with empty mapping."""
    json_data = {
        "conversations": [{
            "title": "Empty Chat",
            "mapping": {}
        }]
    }
    
    json_file = tmp_path / "empty.json"
    json_file.write_text(json.dumps(json_data))
    
    conversations = repository.load_conversations(json_file)
    assert len(conversations) == 0


def test_load_conversations_invalid_message(repository, tmp_path):
    """Test handling of invalid message structures."""
    json_data = {
        "conversations": [{
            "title": "Invalid Messages",
            "mapping": {
                "msg1": "not a dict",  # Invalid message structure
                "msg2": {
                    "message": "not a dict"  # Invalid message structure
                },
                "msg3": {
                    "message": {
                        "content": "not a dict",  # Invalid content structure
                        "author": {"role": "user"}
                    }
                },
                "msg4": {
                    "message": {
                        "content": {"parts": []},  # Empty content
                        "author": {"role": "user"}
                    }
                }
            }
        }]
    }
    
    json_file = tmp_path / "invalid.json"
    json_file.write_text(json.dumps(json_data))
    
    conversations = repository.load_conversations(json_file)
    assert len(conversations) == 1
    assert len(conversations[0].messages) == 0


def test_load_conversations_missing_fields(repository, tmp_path):
    """Test handling of missing optional fields."""
    json_data = {
        "conversations": [{
            "mapping": {
                "msg1": {
                    "message": {
                        "content": {"parts": ["Hello"]},
                        "author": {"role": "user"}
                    }
                }
            }
        }]
    }
    
    json_file = tmp_path / "missing.json"
    json_file.write_text(json.dumps(json_data))
    
    conversations = repository.load_conversations(json_file)
    assert len(conversations) == 1
    
    conv = conversations[0]
    assert conv.title == ""
    assert conv.id == ""
    assert conv.create_time is None
    assert conv.update_time is None
    assert conv.model == ""
    
    msg = conv.messages[0]
    assert msg.message_id == ""
    assert msg.create_time is None


def test_save_conversation_not_implemented(repository, tmp_path):
    """Test that save_conversation raises NotImplementedError."""
    conversation = Conversation(title="Test", messages=[])
    output_file = tmp_path / "output.json"
    
    with pytest.raises(NotImplementedError):
        repository.save_conversation(conversation, output_file) 