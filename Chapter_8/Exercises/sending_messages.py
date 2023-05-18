"""Exercise 8-10"""


def show_messages(messages):
    """Print all messages in the list."""
    print("Showing all messages:")
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """print each message, and move it to sent_messages."""
    print("Sending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


texts = ["Hi I'm Bardia.", "Wassup nigga?", "today is today."]
show_messages(texts)

sent_texts = []
send_messages(texts, sent_texts)

print("\nFinal lists:")
print(texts)
print(sent_texts)
