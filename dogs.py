class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting. ")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


mydog = Dog('Bob', 6)
yourdog = Dog('willie', 5)
mydog.sit()
mydog.roll_over()
print("Your dog's name is " + yourdog.name.title() + ".")
print("Your dog is " + str(yourdog.age) + " years old. ")
print("My dog is " + str(mydog.age) + " years old. ")
yourdog.sit()

print("\nExercise 9-1")


# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.
class Restaurant():
    """Restaurant should store two attributes: a restaurant_name and a cuisine_type."""

    def __init__(self, name, cuisine):
        self.name = name.title()
        self.cuisine = cuisine.title()

    def describe_restaurant(self):
        message = f"{self.name} serves wonderful {self.cuisine} ."
        print(f"\n{message}")

    def open_restaurant(self):
        message = f"{self.name} is now open!"
        print(f"\n{message}")


restaurant = Restaurant('Luigi', 'pizza')
print(restaurant.name)
print(restaurant.cuisine)

restaurant.describe_restaurant()
restaurant.open_restaurant()


class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
my_new_car = Car('audi', 'q5', 2014)
print(my_new_car.get_descriptive_name())