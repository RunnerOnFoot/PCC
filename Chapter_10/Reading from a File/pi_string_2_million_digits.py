"""Large Files: One Million Digits"""

from pathlib import Path

path = Path(
    r'C:\Users\parsa\VSCode\PCC\Chapter_10\Reading from a File\pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''.join(line.strip() for line in lines)

print(f'{pi_string[:52]}...')
print(len(pi_string))
