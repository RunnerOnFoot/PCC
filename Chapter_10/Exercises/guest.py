"""Exercise 10-4"""

from pathlib import Path

path = Path(r'C:\Users\parsa\VSCode\PCC\Chapter_10\Exercises\guest.txt')
USERNAME_PROMPT = "Hi, what's your name? "

print("Hi. You can tell me your name, and I will print it for you :)")
print("(Enter 'q' to quit.)\n")

usernames = []
while True:
    username = input(USERNAME_PROMPT)

    if username == 'q':
        break  # Exit the loop when 'q' is entered
    else:
        print(f"Your username is {username.title()}.")
        print("Welcome back!\n")
        usernames.append(username.title())

# Write usernames to the file
path.write_text('\n'.join(line for line in usernames), encoding='utf-8')
## path.write_text('\n'.join(usernames), encoding='utf-8') -- both is the same!
## WHY???? because of how .join() method works! it's built-in and default.
## but what about each username goes to an individual line?
## Aha i understand it now! it's because of 'n' (new line).

print("Usernames have been written to the file successfully.")
