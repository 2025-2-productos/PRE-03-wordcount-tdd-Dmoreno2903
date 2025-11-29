import os
from typing import Dict


def write_word_counts(output_folder: str, word_counts: Dict[str, int]) -> None:
    """Guarda el conteo de palabras en un archivo de texto en la carpeta de salida especificada.
    
    Args:
        output_folder (str): La carpeta donde se guardará el archivo de conteo de palabras.
        word_counts (Dict[str, int]): Un diccionario con palabras como claves y sus conteos como valores.
    """
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, "wordcount.tsv")
    
    with open(output_file, "w", encoding="utf-8") as file:
        for word, count in word_counts.items():
            file.write(f"{word}\t{count}\n")