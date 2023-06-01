"""
Second Program
Using "json.dumps()" in first program
and Using "json.loads()" in second program.
"""

# We’ll write a program that uses json.loads() to read the list back into memory.
from pathlib import Path
import json

path = Path(r'Chapter_10\storing_data\numbers.json')
contents = path.read_text(encoding='utf-8')
numbers = json.loads(contents)

print(numbers)
