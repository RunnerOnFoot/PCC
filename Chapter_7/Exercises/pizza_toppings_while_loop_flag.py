# 7-4
prompt = "\nWhat toppings you want in your pizza? "
prompt += "\n(Enter 'quit' when you are finished.) "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(f"    I'll add {message}")
