"""Writing Multiple Lines"""

# pylint: disable=invalid-name
from pathlib import Path

contents = "I love programming. \n"
contents += "I love creating new games. \n"
contents += "I also love working with data. \n"

path = Path(
    r'C:\Users\parsa\VSCode\PCC\Chapter_10\writing_to_a_file\programming.txt')
path.write_text(contents, encoding='utf-8')
