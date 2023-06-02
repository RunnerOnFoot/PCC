"""Using json.loads()"""

from pathlib import Path
import json

path = Path(r'Chapter_10\storing_data\retrain\numbers.json')
contents = path.read_text(encoding='utf-8')
numbers = json.loads(contents)

print(numbers)
