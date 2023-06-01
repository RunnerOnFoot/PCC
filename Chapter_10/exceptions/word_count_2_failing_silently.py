"""
Failing Silently
Sometimes, you'll want the program to fail silently when an exception occurs 
and continue on as if nothing happened. To make a program fail silently, 
you write a try block as usual,
but you explicitly tell Python to do nothing in the except block. 
Python has a pass statement that tells it to do nothing in a block.
"""

from pathlib import Path


def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"You file {path} has about {num_words} words.")


filenames = [r'Chapter_10\exceptions\alice.txt', r'Chapter_10\exceptions\moby_dick.txt',
             r'little_women.txt', r'Chapter_10\exceptions\siddhartha.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
