# 7-10
NAME_PROMPT = "\nWhat's your name? "
PLACE_PROMPT = "If you could visit one place in the world, where would it be? "
CONTINUE_PROMPT = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}.
responses = {}

while True:
    # Ask the user where they'd like to go.
    name = input(NAME_PROMPT)
    place = input(PLACE_PROMPT)

    # Store the response.
    responses[name] = place

    # Ask if there's anyone else responding.
    repeat = input(CONTINUE_PROMPT)
    if repeat != 'yes':
        break

# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
