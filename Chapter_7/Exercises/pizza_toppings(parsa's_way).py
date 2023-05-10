# 7-4
prompt = "What toppings you want in your pizza? "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(f"    I'll add {message}")
