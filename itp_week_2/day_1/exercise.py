# ITP Week 2 Day 1 Exercise


# Dictionary Loop

inventory = {
    "soda_cans": 45,
    "chips": 12,
    "sandwiches": 34,
    "candy": 1
}

# SCENARIO: A person came in and bought one of everything!

for item in inventory:
    # decrement item by using an assignment operator (Day 2 Lecture line #130)
    inventory[item] -= 1
    # NOTE: recall that item represents the key of the key:value pair

# SCENARIO: REMOVE ANY 0 ITEMS

# for item in inventory:
for key, value in dict(inventory).items():
    # use an if statement to check if the value is 0 and then remove it
    if value == 0:
        del inventory[key]
print(inventory)
#If your group has completed the above exercise, move on to tuples, sets and nested dictionaries

dogs = {
    "large": {
        "Dozer": {
            "breed": "Shepherd"
        },
        "Tank": {
            "breed": "Mastif"
        }
    },
    "small": {
        "Cujo": {
            "breed": "Bichon Frise"
        },
        "Batman": {
            "breed": "Corgi"
        }
    }
}

# Loop through the dogs dictionary and create a SET of dog names.
dog_names = set()
for dog in dogs:
    for name in dogs[dog]:
        dog_names.add(name)

print(dog_names)

# Loop through the dogs and create a TUPLE combining each dog's name with its breed.
for dog in dogs:
    for name in dogs[dog]:
        print((name, dogs[dog][name]["breed"]))
