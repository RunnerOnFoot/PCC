# 7-4
prompt = "\nWhat toppings you want in your pizza? "
prompt += "\n(Enter 'quit' when you are finished.) "

message = ""
while message != 'quit':
    message = input(prompt)
    print(f"    I'll add {message}")
# This program works well,
# except that it prints the word 'quit' as if it were an actual message.
