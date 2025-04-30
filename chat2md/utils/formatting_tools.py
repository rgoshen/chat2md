from datetime import datetime


def format_timestamp(timestamp):
    """
    Format a UNIX timestamp into a human-readable string

    Args:
        timestamp (float): UNIX timestamp

    Returns:
        str: Formatted timestamp string
    """
    if not timestamp:
        return ""
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M UTC')
