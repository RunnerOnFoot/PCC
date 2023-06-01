"""
Exercise 10-9
Modify your except block in Exercise 10-7 
to fail silently if either file is missing.
"""

from pathlib import Path


def read_file(path):
    """Reads the text files from the path and then prints it."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        print(f"\nFile {path}:")
        print(contents)


filenames = [r'Chapter_10\Exercises\cats.txt',
             r'Chapter_10\Exercises\dogzs.txt']
for filename in filenames:
    filename = Path(filename)
    read_file(filename)
