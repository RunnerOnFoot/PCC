"""Reading the Contents of a File (chained methods)"""


from pathlib import Path

path = Path(
    r'C:/Users/parsa/VSCode/PCC/Chapter_10/Reading from a File/pi_digits.txt')

contents = path.read_text().rstrip()
print(contents)

# We can strip the trailing newline character when we read the contents of the file,
# by applying the rstrip() method immediately after calling read_text():

# contents = path.read_text().rstrip()
