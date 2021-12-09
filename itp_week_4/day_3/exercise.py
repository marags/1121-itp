# ITP Week 4 Day 3 Exercise

# need my imports: json, requests, openxl
import json
import requests
import openpyxl

# create global variable for pokemon list
pokemon_list = []

# function that returns a list of pokemon names and an api to call for skills
# Input: Url
# define function: populate_pokemon(url)
def populate_pokemon(url):
    # make a request
    # assign response to variable
    r = requests.get(url)

    # convert to json
    data = json.loads(r.text)
    # loop/iterate through response data
    for item in data['results']:
        # append data to pokemon list
        pokemon_list.append(item)

# Output: Updated List

# TEST POKEMON API RESPONSE DATA


# THIS FUNCTION TAKES A LONG TIME****

        # BONUS: THIS IS AN EXIT CASE, NEEDED FOR RECURSIVE FUNCTIONS
            # BONUS: THIS IS A RECURSIVE FUNCTION


# Create function called "add_rows" which will take arguments for row_num, name, skills add them to list to list
# function that takes in row_num, name, and skills
    # returns nothing

#FUNCTION 1:
# function that returns the string of the abilities from a list of abilities provided from the API
# function that takes every pokemon retrieve the skills list
# define function called "retrieve_abilities" using an argument of the URL
# assign request to variable
    #return json data using the 'abilities' as a key

#FUNCTION 2:
# create function called "stringify_abilities" which recieves a list(abilities) as argument
    #assign result to empty string
    #define variable called 'first' that will be set to a boolean of True
    # Iterate/loop through the abilities list
        # if first is true
            #result += ability['ability']['name']
        #else
            #take the result += a ',', + ability['ability']['name']
    # return the result


#FUNCTION 3:
    #will uses function 1 & 2 to create pokemon list
        #assign name to a value
        #assign abilities using abilities list USING FUNCTION #1
        #stringify abilities using FUNCTION 2
        # Call the addrow function

# define my workbook
# define worksheet

# skills need to be a string of all the skills comma separated

# final sequence of commands
populate_pokemon("https://pokeapi.co/api/v2/pokemon/")
print(pokemon_list)
#process_pokemon_data()
# save workbook to an xlsx file
#wb.save("/home/dkayzee/vit/intro-python-august-2021/itp_week_4/day_3/output.xlsx")