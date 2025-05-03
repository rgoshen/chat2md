class Chat2MDError(Exception):
    """Base exception for all chat2md errors."""
    pass


class ConversationError(Chat2MDError):
    """Raised when there is an error processing a conversation."""
    pass


class RepositoryError(Chat2MDError):
    """Raised when there is an error with the repository operations."""
    pass


class FormatterError(Chat2MDError):
    """Raised when there is an error formatting the output."""
    pass
