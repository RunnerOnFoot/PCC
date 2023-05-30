"""Exercise 10-3"""

from pathlib import Path

path = Path(
    r'C:\Users\parsa\VSCode\PCC\Chapter_10\Exercises\learning_python.txt')
contents = path.read_text()

for line in contents.splitlines():
    line = line.replace('Python', 'C')
    print(line)
