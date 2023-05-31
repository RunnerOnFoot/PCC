"""Not Handling the FileNotFoundError Exception"""

from pathlib import Path

path = Path(r'C:\Users\parsa\VSCode\PCC\Chapter_10\exceptions\alice.txt')
contents = path.read_text(encoding='utf-8')
