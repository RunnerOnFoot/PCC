"""Working with Multiple Files"""

from pathlib import Path


def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the {path} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"Your file {path} has about {num_words} words.")


filenames = [r'Chapter_10\exceptions\alice.txt', r'siddhartha.txt',
             r'moby_dick.txt', r'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
