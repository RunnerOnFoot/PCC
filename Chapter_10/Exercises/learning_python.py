"""Exercise 10-1"""

from pathlib import Path

print("--- Reading in the entire file:")
path = Path(
    r'C:\Users\parsa\VSCode\PCC\Chapter_10\Exercises\learning_python.txt')
contents = path.read_text()
print(contents)

print("\n--- looping over the lines:")
lines = contents.splitlines()
for line in lines:
    print(line)
