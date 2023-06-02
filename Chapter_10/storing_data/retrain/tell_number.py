"""Reading User-Generated Data"""

from pathlib import Path
import json

path = Path(r'Chapter_10\storing_data\retrain\user_number.json')
contents = path.read_text(encoding='utf-8')
user_number = json.loads(contents)

print(f"Hello, this is your given number: {user_number}")
