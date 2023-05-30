"""Exercise 10-3 making simpler code for pi_string.py"""

from pathlib import Path

path = Path(
    r'C:\Users\parsa\VSCode\PCC\Chapter_10\Reading from a File\pi_million_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))
