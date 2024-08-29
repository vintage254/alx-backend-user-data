#!/usr/bin/env python3
"""
 Regex-ing
"""
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in the log message.

    Args:
    fields (List[str]): List of strings representing fields to obfuscate.
    redaction (str): String to replace the field values with.
    message (str): The log message to obfuscate.
    separator (str): The character separating fields in the log message.

    Returns:
    str: The log message with specified fields obfuscated.
    """
    pattern = f'({"|".join(fields)})=[^{separator}]*'
    return re.sub(pattern, f'\\1={redaction}', message)
