#  03/20/2021 looping thorugh a Dictionary

my_car = {"brand": "Ford", "model": "Mustang", "year": 1964 }

for key in my_car:
    print("_____________________")
    print(f"key in this iteration is: {key}")
    print(f"value of this key is: {my_car[key]}")

print("2 ______________________")
for key in my_car.keys():
    print("--------2-----------")
    print(f"key in this iteration is: {key}")
    print(f"value in this iteration is: {my_car[key]} ")


friends = ['john', 'jane']
print(friends)
sorted_friends = sorted(friends)
friends.sort()
print(sorted_friends)
print(friends)


favorite_languages = { 'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(f"{name}'s favorite language is {favorite_languages[name]}")

rivers = {'nile': 'egypt', 'tigres': 'iraq', 'amazon': 'brazil', 'mississippi': 'usa'}
for river, country in rivers.items():
    print(f"The " + river.title() +  " runs through " + country.title() + "." )
print("\nThese rivers are included in this dictionary:")
for river in rivers.keys():
    print("- " + river.title())


