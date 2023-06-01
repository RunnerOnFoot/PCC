"""
First Program
Using "json.dumps()" in first program
and "json.loads()" in second program.
"""
from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path(r'Chapter_10\storing_data\numbers.json')
contents = json.dumps(numbers)
path.write_text(contents, encoding='utf-8')
