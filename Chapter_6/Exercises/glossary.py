# 6-3

glossary = {
    "string": "A series of characters.",
    "comment": "A note in a program that the Python interpreter ignores.",
    "list": "A collection of items in a particular order.",
    "loop": "Work through a collection of items, one at a time.",
    "dictionary": "A collection of key-value pairs.",
}

word = "string"
print(f"\n{word.title()}: {glossary['string']}")

word = "comment"
print(f"\n{word.title()}: {glossary['comment']}")

word = "list"
print(f"\n{word.title()}: {glossary['list']}")

word = "loop"
print(f"\n{word.title()}: {glossary['loop']}")

word = "dictionary"
print(f"\n{word.title()}: {glossary['dictionary']}")

# another way:
print("\n################################")
for k, v in glossary.items():
    print(f"\n{k.title()}: {v}")
