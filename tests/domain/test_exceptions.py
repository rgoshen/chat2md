import pytest

from chat2md.domain.exceptions import (
    Chat2MDError,
    ConversationError,
    FormatterError,
    RepositoryError
)


def test_chat2md_error_base():
    """Test that Chat2MDError works as a base exception."""
    with pytest.raises(Chat2MDError):
        raise Chat2MDError("Test error")


def test_conversation_error():
    """Test ConversationError inheritance and message."""
    error_msg = "Failed to process conversation"
    with pytest.raises(ConversationError) as exc_info:
        raise ConversationError(error_msg)
    
    assert str(exc_info.value) == error_msg
    assert isinstance(exc_info.value, Chat2MDError)


def test_repository_error():
    """Test RepositoryError inheritance and message."""
    error_msg = "Failed to load repository"
    with pytest.raises(RepositoryError) as exc_info:
        raise RepositoryError(error_msg)
    
    assert str(exc_info.value) == error_msg
    assert isinstance(exc_info.value, Chat2MDError)


def test_formatter_error():
    """Test FormatterError inheritance and message."""
    error_msg = "Failed to format output"
    with pytest.raises(FormatterError) as exc_info:
        raise FormatterError(error_msg)
    
    assert str(exc_info.value) == error_msg
    assert isinstance(exc_info.value, Chat2MDError)


def test_exception_chaining():
    """Test that exceptions can be chained properly."""
    original_error = ValueError("Original error")
    try:
        raise ConversationError("Wrapped error") from original_error
    except ConversationError as e:
        assert isinstance(e.__cause__, ValueError)
        assert str(e.__cause__) == "Original error" 