"""Exercise 10-3 making simpler code for file_reader.py"""

from pathlib import Path

path = Path(
    r'C:/Users/parsa/VSCode/PCC/Chapter_10/Reading from a File/pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)
