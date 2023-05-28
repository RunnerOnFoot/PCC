"""
Exercise 9-15 (second try)
"""

from random import choice


def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = []

    # We don't want to repeat winning numbers or letters, so we'll use a
    #   while loop.
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled_item to the winning_ticket if it hasn't
        #   already been pulled.
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket


def check_ticket(played_ticket, winning_ticket):
    """
    Check all elements in the played_ticket. If any are not in the
    winning_ticket, return False."""
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    # We must have a winning ticket!
    return True


def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = []
    # We don't want to repeat numbers or letters, so we'll use a while loop.
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled_item to the ticket if it hasn't already
        #   been pulled.
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


odds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
leading_ticket = get_winning_ticket(odds)

PLAYS = 0
WON = False

# Let's set a max number of tries, in case this takes forever!
MAX_TRIES = 1_000_000

while not WON:
    new_ticket = make_random_ticket(odds)
    WON = check_ticket(new_ticket, leading_ticket)
    PLAYS += 1
    if PLAYS >= MAX_TRIES:
        break

if WON:
    print("we have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {leading_ticket}")
    print(f"It only took {PLAYS} tries to win!")
else:
    print(f"Tried {PLAYS} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {leading_ticket}")
