"""Reading the Contents of a File"""

from pathlib import Path

path = Path(
    'C:/Users/parsa/VSCode/PCC/Chapter_10/Reading from a File/pi_digits.txt')
contents = path.read_text()
print(contents)
