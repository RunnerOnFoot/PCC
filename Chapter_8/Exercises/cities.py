"""Exercise 8-5"""


def describe_city(city_name, country='england'):
    """Describe a city."""
    msg = f"\n{city_name.title()} is in {country.title()}."
    print(msg)


describe_city('london')
describe_city('manchester')
describe_city(city_name='berlin', country='germany')
describe_city('paris', 'france')
