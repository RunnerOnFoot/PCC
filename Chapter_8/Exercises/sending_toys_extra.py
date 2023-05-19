"""training for myself"""


def show_toys(toys):
    """Print all toys in the list."""

    print("\nShowing all toys:")
    for toy in toys:
        print(toy.title())


def send_toys(toys, sent_toys):
    """Print each toy, and move it to sent_toys."""

    print("\nSending all toys:")
    while toys:
        current_toy = toys.pop()
        print(current_toy.title())
        sent_toys.append(current_toy)


dolls = ['batman', 'spider-man', 'venom', 'horse', 'monkey', 'giraffe']
show_toys(dolls)

sent_dolls = []
send_toys(dolls, sent_dolls)

print("\nFinal lists:")
print(dolls)
print(sent_dolls)
