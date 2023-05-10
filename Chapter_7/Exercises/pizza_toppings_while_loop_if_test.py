# 7-4
prompt = "\nWhat toppings you want in your pizza? "
prompt += "\n(Enter 'quit' when you are finished.) "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(f"    I'll add {message}")
# Now the program makes a quick check before displaying the message;
# and only prints the message if it does not match the quit value.
