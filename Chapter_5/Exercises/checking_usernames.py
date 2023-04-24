# 5-10
current_users = ["parsa", "maryam", "pani", "parnian", "bardia"]
new_users = ["mehrina", "sarvenaz", "parsa", "ali", "bardia"]

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"\nSorry {new_user}, you need to enter a new username!")
    else:
        print(f"\nGreat, {new_user} is still available.")
