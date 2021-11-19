# ITP Week 1 Day 4 Exercise


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

for item in inventory:
    # use an if statement to check if the value is 0 and then remove it
    if inventory[item] == 0:
        pass
        #inventory.pop(item) or del inventory[item] only works in Python 2
