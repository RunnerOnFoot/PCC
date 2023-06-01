"""Exercise 10-10 (first try)"""

from pathlib import Path


def read_file(path):
    """Reads the text files from the path and then prints it."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        counts = contents.lower().count('the')
        print(f"\nI found {counts} 'the' in the file {path}.")

        counts = contents.lower().count('the ')
        print(f"I found {counts} 'the ' in the file {path}.")


filenames = [r'Chapter_10\Exercises\the_brothers_karamazov.txt',
             r'Chapter_10\Exercises\the_count_of_monte_cristo.txt',
             r'Chapter_10\Exercises\little_women.txt']

for filename in filenames:
    filename = Path(filename)
    read_file(filename)
