"""Exercise 10-2"""

from pathlib import Path

path = Path(
    r'C:\Users\parsa\VSCode\PCC\Chapter_10\Exercises\learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    line = line.replace('Python', 'C')
    print(line)
