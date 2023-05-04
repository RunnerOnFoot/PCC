# 6-9
favorite_places = {
    'alex': ['pisa', 'caspian sea'],
    'adolf': ['london eye', 'goldarn tower', 'downtown london'],
    'tom': ['amazon forest'],
}

for person, locations in favorite_places.items():
    NAME = person.title()
    print(f"\nHere's {NAME} favorite places:")
    for location in locations:
        print(f"\t{location.title()}")
