"""Exercise 9-14"""

from random import choice


possibilities = [23, 43, 5, 4, 25, 53, 34, 435, 432, 54, 21,
                 'e', 't', 'w', 'd', 'p']

winning_ticket = []
print("Let's see what the winning ticket is...")

# We don't want to repeat winning numbers or letters, so we'll use a
#   while loop
while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)

    # Only add the pulled item to the winning ticket if it hasn't
    #   already been pulled.
    if pulled_item not in winning_ticket:
        if pulled_item == str(pulled_item):
            print(f"  We pulled a {pulled_item.title()}!")
        else:
            print(f"  We pulled a {pulled_item}!")

        winning_ticket.append(pulled_item)


print(f"\nThe final winning ticket is: {winning_ticket}")
