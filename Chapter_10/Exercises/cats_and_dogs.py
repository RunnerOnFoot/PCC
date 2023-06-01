"""Exercise 10-8"""

from pathlib import Path


def read_file(path):
    """Reads the text files from the path and then prints it."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, your file {path} does not exist!")
    else:
        print(f"\nFile {path}:")
        print(contents)


filenames = [r'Chapter_10\Exercises\cats.txt',
             r'Chapter_10\Exercises\dogs.txt']
for filename in filenames:
    filename = Path(filename)
    read_file(filename)
