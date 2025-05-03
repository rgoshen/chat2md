from pathlib import Path

import pytest

from chat2md.infrastructure.config import Config, OutputConfig


def test_default_config():
    """Test that default configuration is created correctly."""
    config = Config()
    assert isinstance(config.output, OutputConfig)
    assert config.default_output_dir == "markdown_output"
    assert config.log_level == "INFO"
    assert config.encoding == "utf-8"


def test_output_config_defaults():
    """Test that OutputConfig defaults are set correctly."""
    output_config = OutputConfig()
    assert output_config.include_metadata is False
    assert output_config.date_format == "%Y-%m-%d"
    assert output_config.time_format == "%H:%M"
    assert output_config.code_block_style == "```"


def test_config_immutability():
    """Test that config values can be changed when needed."""
    config = Config()
    config.log_level = "DEBUG"
    assert config.log_level == "DEBUG"


def test_custom_output_config():
    """Test that custom output configuration works."""
    output_config = OutputConfig(
        include_metadata=True,
        date_format="%d-%m-%Y",
        time_format="%I:%M %p",
        code_block_style="~~~"
    )
    config = Config(output=output_config)
    assert config.output.include_metadata is True
    assert config.output.date_format == "%d-%m-%Y"
    assert config.output.time_format == "%I:%M %p"
    assert config.output.code_block_style == "~~~"


def test_load_from_file_with_none():
    """Test that load_from_file returns default config when no file specified."""
    config = Config.load_from_file(None)
    assert isinstance(config, Config)
    assert config.log_level == "INFO"
