cities = {
    'london': {
        'country': 'England',
        'population': 8_982_000,
        'closest beach': 'Ruislip Lido',
    },
    'istanbul': {
        'country': 'Turkey',
        'population': 15_460_000,
        'closest beach': 'Caddebostan',
    },
    'dubai': {
        'country': 'United Arab Emirates',
        'population': 3_331_000,
        'closest beach': 'Jumeirah',
    },
}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    closest_beach = city_info['closest beach'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  The {closest_beach} beach is nearby.")
