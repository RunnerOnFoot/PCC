"""Using try-except Blocks for handling the ZeroDivisionError"""

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
