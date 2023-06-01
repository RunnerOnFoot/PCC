"""Exercise 10-8 (eric's way)"""

from pathlib import Path

filenames = [r'Chapter_10\Exercises\cats.txt',
             r'Chapter_10\Exercises\dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")

    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")
    else:
        print(contents)
