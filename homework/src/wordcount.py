from homework.src._internals import count_words, split_into_words, count_words, write_word_counts, preprocess_lines, read_all_lines

def main():
    """Count the frequency of the words in the files in the input directory
    """
    import sys
    import os

    if len(sys.argv) != 3:
        print("Usage: python3 -m homework <input_dir> <output_file>")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    all_lines = read_all_lines(input_dir)
    preprocessed_lines = preprocess_lines(all_lines)
    words = split_into_words(preprocessed_lines)
    word_counts = count_words(words)
    write_word_counts(output_folder=output_dir, word_counts=word_counts)