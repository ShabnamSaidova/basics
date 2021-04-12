# 04/03/2021 This file is for executing the cars.py classes

# Execution
# drive() we will not have an access to this function name yet
from cars import Car

mycar = Car("BMW", "530xi", "black")  # Car is the class,
yourcar = Car("Lexus", "Lexus IS", "silver")



mycar.drive()
mycar.set_odometer_reader(50)
mycar.get_description()
yourcar.do_something()
mycar.get_description()
print("***************************")
yourcar.get_description()
yourcar.drive()
yourcar.set_odometer_reader(30)
yourcar.get_description()

## 04/03/2021
print("___Electric car instances______")


class ElecricCar(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)
        self.battery_size = 60

    pass


my_ev = ElecricCar("tesla", "model x", "blue")
my_ev.drive()
my_ev.get_description()
print("Battery size : ", my_ev.battery_size)
mycar.drive()
my_ev.get_description()