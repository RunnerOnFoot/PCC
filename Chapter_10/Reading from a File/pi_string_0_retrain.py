"""Working with a File's Contents"""


from pathlib import Path

path = Path(
    'c:/Users/parsa/VSCode/PCC/Chapter_10/Reading from a File/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line


print(pi_string)
print(len(pi_string))
