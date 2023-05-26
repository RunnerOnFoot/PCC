"""Importing a Module into a Module"""


from car import Car
from electric_car import ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

my_bmw = Car('bmw', '720i', 2022)
print(my_bmw.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'IDK', 2023)
print(my_tesla.get_descriptive_name())
