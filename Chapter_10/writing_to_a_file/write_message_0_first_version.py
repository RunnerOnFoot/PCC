"""Writing a Single Line"""
from pathlib import Path

path = Path(
    r'C:\Users\parsa\VSCode\PCC\Chapter_10\writing_to_a_file\programming.txt')
path.write_text('I love programming.', encoding='utf-8')
