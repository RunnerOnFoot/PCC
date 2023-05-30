"""Is Your Birthday Contained in PI?"""
from pathlib import Path

path = Path(
    r'C:\Users\parsa\VSCode\PCC\Chapter_10\Reading from a File\pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()

pi_string = ''.join(line.strip() for line in lines)

birthday = input("\nEnter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
