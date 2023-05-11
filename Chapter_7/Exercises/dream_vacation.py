# 7-10
responses = {}
# Set a flag to indicate that polling is active.
ACTIVE_POLLING = True

while ACTIVE_POLLING:
    # Prompt for the person's name and response.
    name = input("\nWhat's your name? ")
    response = input(
        "If you could visit one place in the world, where would you go? ")

    # Store the response in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        ACTIVE_POLLING = False

# Polling is complete. Show results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to travel {response.title()}.")
