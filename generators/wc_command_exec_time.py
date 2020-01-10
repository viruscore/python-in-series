"""
The script executing several times wrapped
in docstring source code and measures its
execution time.
"""
code = """
from pathlib import Path


def open_files(files_paths):
    for file_path in files_paths:
        with open(file_path, 'r') as file:
            yield file


def counter_generator(texts):
    for text in texts:
        lines_count = len(text.splitlines())
        words_count = len(text.split())
        characters_count = len(text)

        yield (
            lines_count,
            words_count,
            characters_count
        )


files_paths = Path('data/molecules').rglob('*.pdb')
files = open_files(files_paths)
files_texts = (file.read() for file in files)

for tl, tw, tc in counter_generator(files_texts):
    print(tl, tw, tc)

"""


import timeit
print(timeit.timeit(code, number=3))
