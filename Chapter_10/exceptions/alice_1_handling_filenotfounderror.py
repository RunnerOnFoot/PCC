"""Handling the FileNotFoundError Exception"""

from pathlib import Path

path = Path(r'alice.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
