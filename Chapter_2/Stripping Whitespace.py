# Extra whitespace can be confusing in your programs. To programmers, 'python' and 'python ' look pretty much the same.
# But to a program, they are two different strings.
# Python detects the extra space in 'python ' and considers it significant unless you tell it otherwise.

# It’s important to think about whitespace,
# because often you’ll want to compare two strings to determine whether they are the same.

# Python can look for extra whitespace on the right and left sides of a string.
# To ensure that no whitespace exists on the right side of a string, use the rstrip() method.

favorite_language = 'Python '
print(favorite_language)

# To remove the whitespace from the string temporarily:
favorite_language = 'Python '
print(favorite_language.rstrip())

# To remove the whitespace from the string permanently, you have to associate the stripped value with the variable name:
favorite_language = 'Python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

print("#########################")

# You can also strip whitespace from the left side of a string using the lstrip() method,
# Or from both sides at once using strip():
favorite_car = ' BMW '
print(favorite_car.rstrip())
print(favorite_car.lstrip())
print(favorite_car.strip())
