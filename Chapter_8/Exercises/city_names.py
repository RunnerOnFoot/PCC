"""Exercise 8-6"""


def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    msg = f"\n{city}, {country}"
    return msg.title()


while True:
    print("\nWhich city are you thinking of?")
    print("(enter 'q' any time to quit)")

    city_name = input("City: ")
    if city_name == 'q':
        break

    print(f"\nWhat country does that {city_name.title()} belong to?")

    country_name = input("Country: ")
    if country_name == 'q':
        break

    formatted_info = city_country(city_name, country_name)
    print(formatted_info)
