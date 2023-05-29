"""Reading the Contents of a File"""

from pathlib import Path

path = Path(
    r'C:/Users/parsa/VSCode/PCC/Chapter_10/Reading from a File/pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)
