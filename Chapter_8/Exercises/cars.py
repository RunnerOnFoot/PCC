"""Exercise 8-14"""


def make_car(manufacturer, model, **other_specs):
    """stores information about a car in a dictionary. and then prints it."""
    print("\nCar details:")

    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }

    for spec, value in other_specs.items():
        car_dict[spec] = value

    return car_dict


car_0 = make_car('benz', 'E500',
                 color='white',
                 tow_package=True,
                 motor='3500ml',
                 headlights='popup',
                 year=2016)
print(car_0)
