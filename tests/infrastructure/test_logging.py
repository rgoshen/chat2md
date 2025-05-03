import logging
from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest

from chat2md.infrastructure.config import Config
from chat2md.infrastructure.logging import setup_logging


@pytest.fixture
def temp_log_file():
    """Create a temporary log file."""
    with NamedTemporaryFile(suffix=".log", delete=False) as f:
        yield Path(f.name)
        Path(f.name).unlink()


def test_setup_logging_basic():
    """Test basic logging setup without file."""
    config = Config()
    setup_logging(config)
    logger = logging.getLogger("chat2md")
    
    assert logger.level == logging.INFO
    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], logging.StreamHandler)
    assert not logger.propagate


def test_setup_logging_with_file(temp_log_file):
    """Test logging setup with file output."""
    config = Config()
    setup_logging(config, temp_log_file)
    logger = logging.getLogger("chat2md")
    
    assert len(logger.handlers) == 2
    assert any(isinstance(h, logging.FileHandler) for h in logger.handlers)
    assert temp_log_file.exists()


def test_setup_logging_debug_level():
    """Test logging setup with DEBUG level."""
    config = Config(log_level="DEBUG")
    setup_logging(config)
    logger = logging.getLogger("chat2md")
    
    assert logger.level == logging.DEBUG


def test_log_message_to_file(temp_log_file):
    """Test that messages are properly written to log file."""
    config = Config()
    setup_logging(config, temp_log_file)
    logger = logging.getLogger("chat2md")
    
    test_message = "Test log message"
    logger.info(test_message)
    
    log_content = temp_log_file.read_text()
    assert test_message in log_content


def test_log_formatting():
    """Test that log messages are properly formatted."""
    config = Config()
    setup_logging(config)
    logger = logging.getLogger("chat2md")
    
    # Get the console handler's formatter
    formatter = logger.handlers[0].formatter
    record = logging.LogRecord(
        "chat2md", logging.INFO, "", 0, "Test message", (), None
    )
    
    formatted = formatter.format(record)
    assert "INFO: Test message" in formatted
