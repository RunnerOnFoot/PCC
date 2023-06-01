"""Exercise 10-6"""

print("Hi. give me two numbers and I'll add them together.")
FIRST_NUMBER_PROMPT = "\nFirst number: "
SECOND_NUMBER_PROMPT = "Second number: "

while True:
    try:
        first_number = int(input(FIRST_NUMBER_PROMPT))
        second_number = int(input(SECOND_NUMBER_PROMPT))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    else:
        print("Let's add them...")
        print(f"{first_number} + {second_number} =",
              first_number + second_number)
        break
