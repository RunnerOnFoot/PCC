# 6-6

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

coders = ['monica', 'sarah', 'joe', 'alex', 'phil']

for coder in coders:
    if coder in favorite_languages:
        print(f"Thank you for taking the poll, {coder.title()}!")
    elif coder not in favorite_languages:
        print(f"{coder.title()}, what's your favorite programming language?")