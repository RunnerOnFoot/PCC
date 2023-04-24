usernames = []

if usernames:
    for username in usernames:
        if username.lower() == "admin":
            print("\nHello admin, would you like to see a status report?")
        else:
            print(f"\nHello {username}, thank you for logging in again!")
else:
    print("We need to find some users!")
