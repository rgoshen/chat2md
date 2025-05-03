import logging
import sys
from pathlib import Path
from typing import Optional

from chat2md.infrastructure.config import Config


def setup_logging(config: Config, log_file: Optional[Path] = None) -> None:
    """Configure logging for the application."""
    # Create logger
    logger = logging.getLogger("chat2md")
    
    # Clear existing handlers
    logger.handlers.clear()
    
    logger.setLevel(config.log_level)

    # Create formatters
    console_formatter = logging.Formatter(
        '%(levelname)s: %(message)s'
    )
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # File handler (if log file specified)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    # Prevent propagation to root logger
    logger.propagate = False
