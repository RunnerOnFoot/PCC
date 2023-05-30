"""
Working with a File's Contents.
and using lstring() to delete the whitespace on the left side of the digits
in each line.
"""

from pathlib import Path

path = Path(
    r'c:\Users\parsa\VSCode\PCC\Chapter_10\Reading from a File\pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''

for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

# So the length is shorter now
# because of removing useless whitespaces between the digits.
# And it's showing the pi number correctly :D
