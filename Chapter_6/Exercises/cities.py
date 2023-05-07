# 6-11
cities = {
    'london': {
        'country': 'England',
        'population': 8_982_000,
        'closest beach': 'Ruislip Lido Beach',
    },
    'istanbul': {
        'country': 'Turkey',
        'population': 15_460_000,
        'closest beach': 'Caddebostan Plajı',
    },
    'dubai': {
        'country': 'United Arab Emirates',
        'population': 3_331_000,
        'closest beach': 'Jumeirah Beach',
    },
}

# Print the name of each city and all of the information about them.
for city, information in cities.items():
    print(f'\n"{city.title()}"')
    for k, v in information.items():
        print(f"{k.title()}: {v}")
