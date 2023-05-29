"""Accessing a File's Lines"""

from pathlib import Path

path = Path(
    r'C:/Users/parsa/VSCode/PCC/Chapter_10/Reading from a File/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)
print(lines)
