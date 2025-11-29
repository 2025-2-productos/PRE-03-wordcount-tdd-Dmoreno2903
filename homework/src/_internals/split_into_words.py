
from typing import List


def split_into_words(lines: List[str]) -> List[str]:
    """Split lines into individual words.
    
    Args:
        lines (List[str]): A list of preprocessed lines.
    Returns:
        List[str]: A list of words extracted from the lines.
    """
    words: List[str] = []
    for line in lines:
        line_words = line.split()
        words.extend([word.strip(".,!?:;\"'()[]{}") for word in line_words])
    return words