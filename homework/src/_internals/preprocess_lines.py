from typing import List


def preprocess_lines(lines: List[str]) -> List[str]:
    """Preprocess lines by stripping whitespace and converting to lowercase.
    
    Args:
        lines (List[str]): List of input lines.
    Returns:
        List[str]: Preprocessed lines.
    """
    return [line.strip().lower() for line in lines]