"""Exercise 11-1"""

from city_functions import city_country


def test_city_country():
    """Does a simple city and country pair work?"""
    formatted_location = city_country('santiago', 'chile')
    assert formatted_location == 'Santiago, Chile.'
