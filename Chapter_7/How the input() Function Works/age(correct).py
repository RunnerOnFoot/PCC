# We can resolve this issue by using the int() function,
# which converts the input string to a numerical value.
# This allows the comparison to run successfully:
age = input("How old are you? ")
age = int(age)
print(age >= 18)
