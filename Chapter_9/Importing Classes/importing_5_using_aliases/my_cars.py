"""Using Aliases"""


from electric_car import ElectricCar as EC
import car as CR

my_leaf = EC('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

my_bmw = CR.Car('bmw', '740i', 2024)
print(my_bmw.get_descriptive_name())
