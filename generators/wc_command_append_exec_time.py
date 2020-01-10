"""
The script executing several times wrapped
in docstring source code and measures its
execution time.
"""
code = """
from pathlib import Path


def open_files(files_paths):
    files = []

    for file_path in files_paths:
        files.append(open(file_path, 'r'))

    return files


def read_files(files):
    texts = []

    for file in files:
        texts.append(file.read())
        file.close()

    return texts


def counter(texts):
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


files_paths = Path('data/molecules').rglob('*.pdb')
files = open_files(files_paths)
files_texts = read_files(files)

for tl, tw, tc in counter(files_texts):
    print(tl, tw, tc)
"""


import timeit
print(timeit.timeit(code, number=3))
