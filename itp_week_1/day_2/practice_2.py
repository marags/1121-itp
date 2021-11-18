# ITP Week 1 Day 2 (In-Class) Practice

# This is a number magic trick
# Pick a number from 1 - 9
# Multiple by 2
# Add 10 to the total
# Divide by 2
# Subtract by the original number
# Final number is 5

# Take an user's input
# Assign a new variable for each step
# at the end, use an if statement to see if the final is always 5!

user_entry = int(input("Enter a number from 1 - 9 ")) #no input validation
mult_by_2 = user_entry * 2
add_10 = mult_by_2 + 10
divide_in_half = add_10 // 2 #integer division
final_number = divide_in_half - user_entry
print(final_number)