from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class OutputConfig:
    """Configuration for output formatting."""
    include_metadata: bool = False
    date_format: str = "%Y-%m-%d"
    time_format: str = "%H:%M"
    code_block_style: str = "```"


@dataclass
class Config:
    """Global configuration for chat2md."""
    output: OutputConfig = OutputConfig()
    default_output_dir: str = "markdown_output"
    log_level: str = "INFO"
    encoding: str = "utf-8"

    @classmethod
    def load_from_file(cls, config_path: Optional[Path] = None) -> 'Config':
        """
        Load configuration from a file. If no file is specified,
        return default configuration.
        """
        # TODO: Implement config file loading
        return cls()
