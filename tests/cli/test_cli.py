"""Tests for the CLI module."""
import sys
from unittest.mock import Mock, patch

import pytest

from chat2md.cli import main
from chat2md.domain.exceptions import Chat2MDError


@pytest.fixture
def mock_use_case():
    """Mock for ConvertConversationsUseCase."""
    with patch('chat2md.cli.ConvertConversationsUseCase') as mock:
        instance = Mock()
        # Set a default return value for execute
        instance.execute.return_value = [Mock()]
        mock.return_value = instance
        yield instance


@pytest.fixture
def mock_config():
    """Mock for Config."""
    with patch('chat2md.cli.Config') as mock_class:
        instance = Mock()
        instance.default_output_dir = "markdown_output"  # Set a proper string value
        mock_class.load_from_file = Mock(return_value=instance)
        yield mock_class


@pytest.fixture
def mock_setup_logging():
    """Mock for setup_logging."""
    with patch('chat2md.cli.setup_logging') as mock:
        yield mock


def test_successful_conversion(mock_use_case, mock_config, mock_setup_logging, tmp_path):
    """Test basic successful conversion."""
    # Setup
    input_file = tmp_path / "conversations.json"
    input_file.touch()
    output_files = [tmp_path / "test1.md", tmp_path / "test2.md"]
    mock_use_case.execute.return_value = output_files

    # Run
    with patch.object(sys, 'argv', ['chat2md', str(input_file)]):
        result = main()

    # Assert
    assert result == 0
    mock_use_case.execute.assert_called_once()
    args = mock_use_case.execute.call_args[1]
    assert args['source_path'] == input_file
    assert not args['include_metadata']


def test_full_metadata_flag(mock_use_case, mock_config, mock_setup_logging, tmp_path):
    """Test conversion with full metadata flag."""
    # Setup
    input_file = tmp_path / "conversations.json"
    input_file.touch()
    output_files = [tmp_path / "test1.md"]
    mock_use_case.execute.return_value = output_files

    # Run
    with patch.object(sys, 'argv', ['chat2md', str(input_file), '--full-meta']):
        result = main()

    # Assert
    assert result == 0
    args = mock_use_case.execute.call_args[1]
    assert args['include_metadata']


def test_config_file(mock_use_case, mock_config, mock_setup_logging, tmp_path):
    """Test using a config file."""
    # Setup
    input_file = tmp_path / "conversations.json"
    config_file = tmp_path / "config.json"
    input_file.touch()
    config_file.touch()
    output_files = [tmp_path / "test1.md"]
    mock_use_case.execute.return_value = output_files

    # Run
    with patch.object(sys, 'argv', ['chat2md', str(input_file), '--config', str(config_file)]):
        result = main()

    # Assert
    assert result == 0
    mock_config.load_from_file.assert_called_once_with(config_file)


def test_log_file(mock_use_case, mock_config, mock_setup_logging, tmp_path):
    """Test logging to a file."""
    # Setup
    input_file = tmp_path / "conversations.json"
    log_file = tmp_path / "chat2md.log"
    input_file.touch()
    output_files = [tmp_path / "test1.md"]
    mock_use_case.execute.return_value = output_files

    # Run
    with patch.object(sys, 'argv', ['chat2md', str(input_file), '--log-file', str(log_file)]):
        result = main()

    # Assert
    assert result == 0
    mock_setup_logging.assert_called_once()
    assert mock_setup_logging.call_args[0][1] == log_file


def test_verbose_mode(mock_use_case, mock_config, mock_setup_logging, tmp_path):
    """Test verbose logging mode."""
    # Setup
    input_file = tmp_path / "conversations.json"
    input_file.touch()
    output_files = [tmp_path / "test1.md"]
    mock_use_case.execute.return_value = output_files
    config_instance = mock_config.load_from_file.return_value

    # Run
    with patch.object(sys, 'argv', ['chat2md', str(input_file), '--verbose']):
        result = main()

    # Assert
    assert result == 0
    assert config_instance.log_level == "DEBUG"


def test_chat2md_error(mock_use_case, mock_config, mock_setup_logging, tmp_path):
    """Test handling of Chat2MDError."""
    # Setup
    input_file = tmp_path / "conversations.json"
    input_file.touch()
    mock_use_case.execute.side_effect = Chat2MDError("Test error")

    # Run
    with patch.object(sys, 'argv', ['chat2md', str(input_file)]):
        result = main()

    # Assert
    assert result == 1


def test_unexpected_error(mock_use_case, mock_config, mock_setup_logging, tmp_path):
    """Test handling of unexpected errors."""
    # Setup
    input_file = tmp_path / "conversations.json"
    input_file.touch()
    mock_use_case.execute.side_effect = Exception("Unexpected error")

    # Run
    with patch.object(sys, 'argv', ['chat2md', str(input_file)]):
        result = main()

    # Assert
    assert result == 1


def test_missing_input_file(mock_use_case, mock_config, mock_setup_logging):
    """Test error when input file is missing."""
    # Run
    with pytest.raises(SystemExit):
        with patch.object(sys, 'argv', ['chat2md']):
            main()
