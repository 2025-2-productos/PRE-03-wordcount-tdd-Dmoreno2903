import os
from typing import List


def read_all_lines(input_folder: str) -> List[List[str]]:
    """Read all lines from text files in the specified input folder.
    
    Args:
        input_folder (str): The folder containing text files to read.
    
    Returns:
        List[str]: A list containing all lines from the text files.
    """
    lines: List[str] = []
    filenames: List[str] = os.listdir(input_folder)

    # Iterate through each file in the input folder and save
    # its lines in a list and return it
    for filename in filenames:
        with open(os.path.join(input_folder, filename), "r", encoding="utf-8") as file:
            file_lines = file.readlines()
            lines.extend(file_lines)
    return lines