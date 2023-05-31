"""Analyzing Text (I will test for myself to fully understand!)"""

from pathlib import Path

path = Path(r'Chapter_10\exceptions\alice.txt')
contents = path.read_text(encoding='utf-8')
words = contents.split()
print(words)
print(len(words))
