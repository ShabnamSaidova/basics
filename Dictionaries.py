#######03/18/2021######
#### Dictionaries#######

# print("******Dictionaries******")
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
#
# alien_0 = {'color': 'green', 'points': 5}
# new_points = alien_0['points']
# print("You just earned " + str(new_points) + " points!")
# Key/value pair data structure, since each element comes as (key: value)
# Create, access, modify (add/remove/update elements)
# looping this data structure
# some mostly used builtin functions
my_friend = {}
my_house = dict()
my_car = {"brand": "Ford", "model": "Mustang", "year": 1964, 1: "value of 1"}
print(my_car["brand"])
print(f"the value of key 'brand' is: {my_car['brand']}.")

# adding the value
my_car['price'] = 125000.00
print(" price is added ------")
print(my_car)
 # updating the value in dictionary
print("Price was updated.")
my_car['price'] = 120000.00
print(my_car)

# removing the values from dictionary
print("element with key 1 is being removed ------")
del my_car[1]
print(my_car)

print("Exercise 6-1")
# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.

amigo = {"first_name": "Vitaly", "last_name": "Didkivskiy", "age": 19, "city": "Florence"}
print(f"my friend's first name is : {amigo['first_name']}")
print(f"my friend's last name is : {amigo['last_name']}")
print(f"my friend's age is : {amigo['age']}")
print(f"my friend lives in  : {amigo['city']}")

print("Exercise 6-2")
# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.

favorite_numbers = {'mary': 5, 'stanley': 20, 'joseph': 7, 'jennifer': 13, 'sarah': 52}
num = favorite_numbers['mary']
print(f"Mary's favorite number is {num}.")
num = favorite_numbers['stanley']
print(f"Stanley's favorite number is {num}.")
num =  favorite_numbers['joseph']
print(f"Joseph's favorite number is {num}.")
num = favorite_numbers['jennifer']
print(f"Jennifer's favorite number is {num}.")
num = favorite_numbers['sarah']
print(f"Sarah's favorite number is {num}.")

print("Exercise 6-3")
# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.
# glossary = {"variables": "Containers for storing data values",
#             "lists": "A collection of items in a particular order",
#             "loop": "Sequence of instructions that get executed multiple times until a certain condition is reached",
#             "dictionaries": "A collection of key-value pairs",
#             "integer" : "Name used for a numeric value"}
# word = 'variables'
# print(f"\n{word.title()}: {glossary[word]}.")
# word = 'lists'
# print(f"\n{word.title()}: {glossary[word]}.")
# word = 'loop'
# print(f"\n{word.title()}: {glossary[word]}.")
# word = 'dictionaries'
# print(f"\n{word.title()}: {glossary[word]}.")
# word = 'integer'
# print(f"\n{word.title()}: {glossary[word]}.")
#
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x_position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

#The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']))

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',}
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")
user_0 ={'username': 'efermi',
         'first': 'enrico',
         'last': 'fermi',
         }
for key, value in user_0.items():
    print("\nKey: " + key)
    print("\nValue: " + value)



favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',}
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")




favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("  Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")





favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("Looping Through a Dictionary’s Keys in Order")
favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# print("Looping Through All Values in a Dictionary")
# favorite_languages = {'jen': 'python',
#                       'sarah': 'c',
#                       'edward': 'ruby',
#                       'phil': 'python',
#                       }
# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }
for language in set(favorite_languages.values()):
    print(language.title())

# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.
print("\n Exercise 6-4 ")
glossary = {"variables": "Containers for storing data values",
            "lists": "A collection of items in a particular order",
            "loop": "Sequence of instructions that get executed multiple times until a certain condition is reached",
            "dictionaries": "A collection of key-value pairs",
            "integer" : "Name used for a numeric value"}
for word in sorted(glossary.keys()):
    print(word.title())
for meaning in glossary.values():
    print(meaning)