# ITP Week 4 Day 3 Exercise

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
    response = requests.get(url)
    # convert to json
    data = json.loads(response.text)
    # loop/iterate through response data

    for item in data['results']:
        # append data to  pokemon list
        pokemon_list.append(item)
# Output: Updated List

# TEST POKEMON API RESPONSE DATA
populate_pokemon("https://pokeapi.co/api/v2/pokemon/")

# THIS FUNCTION TAKES A LONG TIME****

        # BONUS: THIS IS AN EXIT CASE, NEEDED FOR RECURSIVE FUNCTIONS
            # BONUS: THIS IS A RECURSIVE FUNCTION

#FUNCTION 1:
# function that returns the string of the abilities from a list of abilities provided from the API
# function that takes every pokemon retrieve the skills list
# define function called "retrieve_abilities" using an argument of the URL
def retrieve_abilities(url):
    results = requests.get(url)
    data = json.loads(results.text)
    print("Getting abilities...")
    return data['abilities']

# assign request to variable
    #return json data using the 'abilities' as a key

#FUNCTION 2:
# create function called "stringify_abilities" which recieves a list(abilities) as argument
def stringify_abilities(abilities):
    #assign result to empty string
    result = ''
    #define variable called 'first' that will be set to a boolean of True
    first = True
    # Iterate/loop through the abilities list
    for ability in abilities:
        # if first is true
        if first == True:
            result += ability['ability']['name']    
        else:
            #take the result += ',' + ability['ability']['name']
           result +=  ',' + ability['ability']['name'] 
    # return the result
    print("Returning abilites list...")
    return result
# Create function called "add_rows" which will take arguments for row_num, name, skills add them to list to list
# function that takes in row_num, name, and skills
def add_rows(row_num, name, skills):
    sheet["A" + str(row_num)] = name
    sheet["B" + str(row_num)] = skills
    print("Adding rows...")
    # returns nothing

#FUNCTION 3:
    #will uses function 1 & 2 to create pokemon list
def process_pokemon_data():
    print("Processing Pokemon...")
    for idx, pokemon in enumerate(pokemon_list, start=1):
        name = pokemon['name']
    #assign abilities using abilities list USING FUNCTION #1
        abilities_list = retrieve_abilities(pokemon['url'])
    #stringify abilities using FUNCTION 2
        abilities_string = stringify_abilities(abilities_list)
    # Call the addrow function
        add_rows(idx, name, abilities_string)

# define my workbook
# define worksheet
wb = openpyxl.Workbook()
sheet = wb.active

# skills need to be a string of all the skills comma separated

# final sequence of commands
populate_pokemon("https://pokeapi.co/api/v2/pokemon/")
process_pokemon_data()
# # save workbook to an xlsx file
wb.save("exercise.pyoutput.xlsx")
