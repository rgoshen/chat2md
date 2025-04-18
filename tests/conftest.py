import json
import pytest
from pathlib import Path

@pytest.fixture
def sample_conversation_path():
    return Path(__file__).parent / "fixtures" / "sample_conversations.json"

@pytest.fixture
def sample_conversation_dict(sample_conversation_path):
    with open(sample_conversation_path, "r", encoding="utf-8") as f:
        conversations = json.load(f)
    return { "conversations": conversations }
