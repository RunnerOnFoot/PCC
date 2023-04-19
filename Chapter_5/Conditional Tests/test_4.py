# If case matters, this behavior is advantageous.
# But if case doesn’t matter and instead you just want to test the value of a variable,
# you can convert the variable’s value to lowercase before doing the comparison:
car = "Audi"
print(car.lower() == "audi")

# The lower() method doesn’t change the value that was originally stored in car:
print(car)
