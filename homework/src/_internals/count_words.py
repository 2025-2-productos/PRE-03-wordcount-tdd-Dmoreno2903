from typing import Dict, List


def count_words(words: List[str]) -> Dict[str, int]:
    """Cuenta la frecuencia de cada palabra en la lista dada.
    
    Args:
        words (List[str]): Una lista de palabras.
    
    Returns:
        Dict[str, int]: Un diccionario con palabras como claves y sus conteos como valores.
    """
    word_counts: dict[str, int] = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts