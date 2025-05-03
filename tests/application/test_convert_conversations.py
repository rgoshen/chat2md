from pathlib import Path
from unittest.mock import Mock

import pytest

from chat2md.application.use_cases.convert_conversations import ConvertConversationsUseCase
from chat2md.domain.entities.conversation import Conversation, Message
from chat2md.domain.exceptions import ConversationError, RepositoryError
from chat2md.infrastructure.config import Config


@pytest.fixture
def mock_repository():
    return Mock()


@pytest.fixture
def mock_markdown_converter():
    return Mock()


@pytest.fixture
def config():
    return Config()


@pytest.fixture
def use_case(mock_repository, mock_markdown_converter, config):
    return ConvertConversationsUseCase(
        repository=mock_repository,
        markdown_converter=mock_markdown_converter,
        config=config
    )


def test_successful_conversion(use_case, mock_repository, mock_markdown_converter, tmp_path):
    """Test successful conversion of conversations."""
    # Setup test data
    conversation = Conversation(
        title="Test Conversation",
        messages=[
            Message(author="user", content="Hello"),
            Message(author="assistant", content="Hi there")
        ]
    )
    mock_repository.load_conversations.return_value = [conversation]
    mock_markdown_converter.convert_to_markdown.return_value = "# Test Markdown"

    # Execute use case
    output_files = use_case.execute(
        source_path=Path("test.json"),
        output_dir=tmp_path,
        include_metadata=True
    )

    # Verify results
    assert len(output_files) == 1
    assert output_files[0].name == "Test_Conversation.md"
    assert output_files[0].read_text() == "# Test Markdown"
    mock_markdown_converter.convert_to_markdown.assert_called_once_with(
        conversation,
        include_metadata=True
    )


def test_empty_conversation_skipped(use_case, mock_repository, mock_markdown_converter, tmp_path):
    """Test that empty conversations are skipped."""
    # Setup test data
    empty_conversation = Conversation(title="Empty", messages=[])
    mock_repository.load_conversations.return_value = [empty_conversation]

    # Execute use case
    output_files = use_case.execute(
        source_path=Path("test.json"),
        output_dir=tmp_path
    )

    # Verify results
    assert len(output_files) == 0
    mock_markdown_converter.convert_to_markdown.assert_not_called()


def test_repository_error(use_case, mock_repository, tmp_path):
    """Test handling of repository errors."""
    mock_repository.load_conversations.side_effect = Exception("Failed to load")

    with pytest.raises(RepositoryError) as exc_info:
        use_case.execute(
            source_path=Path("test.json"),
            output_dir=tmp_path
        )
    
    assert "Failed to process conversations" in str(exc_info.value)


def test_conversion_error(use_case, mock_repository, mock_markdown_converter, tmp_path):
    """Test handling of conversion errors."""
    # Setup test data
    conversation = Conversation(
        title="Test",
        messages=[Message(author="user", content="Hello")]
    )
    mock_repository.load_conversations.return_value = [conversation]
    mock_markdown_converter.convert_to_markdown.side_effect = Exception("Conversion failed")

    with pytest.raises(ConversationError) as exc_info:
        use_case.execute(
            source_path=Path("test.json"),
            output_dir=tmp_path
        )
    
    assert "Failed to convert conversation" in str(exc_info.value)


def test_sanitize_filename(use_case):
    """Test filename sanitization."""
    unsafe_filename = 'Test: File/with\\unsafe*chars?'
    safe_filename = use_case._sanitize_filename(unsafe_filename)
    assert safe_filename == 'Test_Filewith_unsafe_chars'
    assert all(c not in safe_filename for c in r'\\/*?:"<>|!')
