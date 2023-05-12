NAME_PROMPT = "\nWhat's your name? "
JOB_PROMPT = "What's the dream job you always wanted? "
CONTINUE_PROMPT = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: Job}.
responses = {}

while True:
    # Ask the user what'd their dream job.
    name = input(NAME_PROMPT)
    job = input(JOB_PROMPT)

    # Store the response.
    responses[name] = job

    # Ask if there's anyone else responding.
    repeat = input(CONTINUE_PROMPT)
    if repeat != 'yes':
        break

# Show results of survey.
print("\n--- Results ---")
for name, job in responses.items():
    print(f"{name.title()} would like to work as a {job.title()}.")
