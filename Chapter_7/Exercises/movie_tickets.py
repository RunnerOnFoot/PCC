# 7-5
PROMPT = "\nHow old are you? "
PROMPT += "\nEnter 'quit' when you are finished: "

ACTIVE = True
while ACTIVE:
    age = input(PROMPT)

    if age == 'quit':
        ACTIVE = False
        break

    age = int(age)

    if age < 3:
        print("The ticket is free :D")
    elif 3 <= age <= 12:
        print("The ticket is 10$")
    elif age > 12:
        print("The ticket is 15$")
