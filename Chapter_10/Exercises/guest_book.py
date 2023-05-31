"""Exercise 10-5"""

from pathlib import Path

path = Path(r'C:\Users\parsa\VSCode\PCC\Chapter_10\Exercises\guest_book.txt')

PROMPT = "\nHi, what's your name? "
PROMPT += "\nEnter 'quit' if your are the last guest. "

guest_names = []
while True:
    name = input(PROMPT)
    if name == 'quit':
        break

    print(f"Thanks {name}, we'll add you to the guest book.")
    guest_names.append(name)

# Build a string where "\n" is added after each name.
file_string = ''
for name in guest_names:
    file_string += f"{name.title()}\n"

path.write_text(file_string, encoding='utf-8')
