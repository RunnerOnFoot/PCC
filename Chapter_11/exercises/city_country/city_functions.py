"""A collection of functions for working with cities."""


def city_country(city, country):
    """
    Return a single string of the form 'City, Country'
    such as 'Santiago, Chile'.
    """
    formatted_location = f"{city}, {country}."
    return formatted_location.title()
