from pathlib import Path


def open_files(files_paths):
    """Opens the files for reading.

    :returns: A buffered text streams in a list.
    :rtype: `list`
    """
    files = []

    for file_path in files_paths:
        files.append(open(file_path, 'r'))

    return files


def read_files(files):
    """Extracts the whole text from the files.

    :returns: A texts in a list.
    :rtype: `list`
    """
    texts = []

    for file in files:
        texts.append(file.read())
        file.close()

    return texts


def counter(texts):
    """Counts the number of lines, words, characters
    for each given text.

    :returns: A texts in a list.
    :rtype: `list`
    """
    results = []

    for text in texts:
        lines_count = len(text.splitlines())
        words_count = len(text.split())
        characters_count = len(text)
        results.append((
            lines_count,
            words_count,
            characters_count
        ))

    return results


# Yielding all matching files.
files_paths = Path('data/molecules').rglob('*.pdb')
# Open the files.
files = open_files(files_paths)
# Read the files.
files_texts = read_files(files)

for tl, tw, tc in counter(files_texts):
    # Prints for each text:
    # 1. Number of lines.
    # 2. Number of words.
    # 3. Number of characters.
    print(tl, tw, tc)
