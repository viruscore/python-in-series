from pathlib import Path


def open_files(files_paths):
    """Opens the files for reading by lazy evaluating them.

    :yields: class:`io.TextIOWrapper`
    """
    for file_path in files_paths:
        with open(file_path, 'r') as file:
            yield file


def counter_generator(texts):
    """Counts the number of lines, words, characters
    for each given text.

    :yields: `tuple`
    """
    for text in texts:
        lines_count = len(text.splitlines())
        words_count = len(text.split())
        characters_count = len(text)

        yield (
            lines_count,
            words_count,
            characters_count
        )


# Yielding all matching files.
files_paths = Path('data/molecules').rglob('*.pdb')
# Open the files.
files = open_files(files_paths)
# Read the files.
files_texts = (file.read() for file in files)

for tl, tw, tc in counter_generator(files_texts):
    # Prints for each text:
    # 1. Number of lines.
    # 2. Number of words.
    # 3. Number of characters.
    print(tl, tw, tc)
