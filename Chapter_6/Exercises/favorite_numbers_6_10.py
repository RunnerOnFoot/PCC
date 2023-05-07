# 6-10

favorite_numbers = {
    "amin": [5, 24, 37],
    "ali": [7],
    "pantea": [10, 26],
    "bardia": [50, 31, 90],
    "parnian": [18, 34],
}

# print eat person's name along with their favorite numbers.
for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        for number in numbers:
            print(f"\n{name.title()}'s favorite number is: {number}")
    else:
        print(f"\n{name.title()}'s favorite numbers are:")
        for number in numbers:
            print(number)
