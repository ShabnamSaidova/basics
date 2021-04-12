# 03/28/2021 Object-oriented Programming Concepts: Class and Object

class Car:
    """This class describes model of the car."""

    def __init__(self, brand, model, color):
        """This is the constructor, with required parameters. """
        self.model = model
        self.color = color
        self.brand = brand
        self.odo_reader = 0

    def set_odometer_reader(self, miles):
        """Function to update the value of """
        self.odo_reader = miles


    def drive(self):
        """driving action"""
        if self.brand.lower() == "bmw":
            print(f"You are driving the car FAST even without DL! isn't it awesome!")
        else:
            print(f"You are driving the car  even without DL! isn't it awesome!")

    def do_something(self):
        print("I want to do something......")
        print(" Let me drive this car ;) ")
        self.drive()

    def get_description(self):
        """"""

        print(f"Model of the car: {self.model}")
        print(f"Color of the car: {self.color}")
        print(f"Brand of the car: {self.brand}")
        print(f"You have {self.odo_reader}  miles on your car.")


# Execution
# drive() we will not have an access to this function name yet
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

#
class ElectricCar(Car):
    """This is an child class of Car. ElectricCar class inherits from Car class."""
    def __init__(self, brand, model, color):
        """this is the constructor, with required parameters."""
        super().__init__(brand, model, color)
        self.battery_size = 60
    def get_battery_info(self):
        print(f"This car has a   {self.battery_size} - kWh battery")

    def get_description(self):
        super().get_description()
        print(f"Battery size of the car: {self.battery_size}")
    def drive(self):
        print("You are driving EV! It's way awesome then just a car, maybe")



