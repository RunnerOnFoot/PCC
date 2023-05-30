"""
Working with a File's Contents.
Using .join() function to make the program more efficient.
And I found a way to how use lstrip() in this method :D
by writing the one line for loop in it!
"""

from pathlib import Path

path = Path(
    r'c:\Users\parsa\VSCode\PCC\Chapter_10\Reading from a File\pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''.join(line.lstrip() for line in lines)
print(pi_string)
print(len(pi_string))
