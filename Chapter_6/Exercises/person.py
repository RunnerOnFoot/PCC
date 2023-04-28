# 6-1

my_friend = {
    "first_name": "masy",
    "last_name": "naji",
    "age": 24,
    "city": "dehli",
}

for k, v in my_friend.items():
    print(k, v)

print("\n")

# another way:
for v in my_friend.values():
    print(v)

# another another way :D

print(my_friend["first_name"])
print(my_friend["last_name"])
print(my_friend["age"])
print(my_friend["city"])
