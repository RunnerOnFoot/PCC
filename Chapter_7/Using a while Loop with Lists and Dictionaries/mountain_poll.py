# FILLING A DICTIONARY WITH USER INPUT #
responses = {}
# Set a flag to indicate that polling is active.
POLLING_ACTIVE = True

while POLLING_ACTIVE:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
<<<<<<< HEAD
    response = input("Which mountain would you like to climb someday? ")
=======
    response = input("\nWhich mountain would you like to climb someday? ")
>>>>>>> b1c2ffd3df5ef54f04484245afe5c91a592361d4

    # Store the response in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        POLLING_ACTIVE = False

# Polling is complete. Show results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")
