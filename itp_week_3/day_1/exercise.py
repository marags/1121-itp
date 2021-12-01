# ITP Week 2 Day 2 Exercise

#Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.

# Easy:
#     - A function that subtracts one integer from another
#     - A function that multiplies three integers
#     - A function that adds four integers
def subtract(a, b):
    print(a - b)
    return a - b #incase use wants to capture value

def mult(a, b, c):
    print(a * b * c)
    return a * b * c

def add(a, b, c, d):
    print(a + b + c + d)
    return a + b + c + d

subtract(10, 5)
mult(2, 2, 2)
add(10, 5, 8, 2)

# Medium: 
#     - Create a calculator function using THREE input parameters (two float, one string[hint: it will be a math symbol]) to allow the user to add, substract, multiply and divide.

def calc(a, b, sym):
    if sym == "-":
        print(a - b)
        return a - b
    elif sym == "+":
        print(a + b)
        return a + b
    elif sym == "*":
        print(a * b)
        return a * b
    elif sym == "/":
        print(a / b)
        return a / b
    elif sym == "//":
        print(a // b)
        return a // b

# Hard: 
#     - You're at a restaurant with some friends and the server didn't split up the check.
# Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax,
# and then divides the total bill by the number of people input by the user.  
# 
# BONUS:  Include an option for adding tip through either a percentage amount assigned to a global varible, or through a specific amount input by the user.

tax_rate = 0.08
def bill_divider(total, people):
    return (total + (total * tax_rate)) // people 

print(bill_divider(100, 4))