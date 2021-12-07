
import openpyxl
import json
import requests

wb = openpyxl.load_workbook("/Users/Dev/Code/Git_Repositories/VetsInTech/Python Fundamentals/1121-itp/itp_week_3/day_4/lecture.xlsx")
r = requests.get("https://rickandmortyapi.com/api/character")
wb.create_sheet("RickAndMorty")
# print(wb.sheetnames)
data = json.loads(r.text)

sheet = wb["RickAndMorty"]
sheet["A1"] = "Name"
sheet["B1"] = "Status"
sheet["C1"] = "Species"
sheet["D1"] = "Gender"


# Create a new worksheet
# assign new worksheet to a variable
# and create the following columns and populate the data from the API
    # Name
    # Status
    # Species
    # Gender

# print(data['results'][0]['name']) 

for i in range(20):
    sheet["A" + str(i + 2)] = data['results'][i]['name']
    sheet["B" + str(i + 2)] = data['results'][i]['status']
    sheet["C" + str(i + 2)] = data['results'][i]['species']
    sheet["D" + str(i + 2)] = data['results'][i]['gender']

wb.save("/Users/Dev/Code/Git_Repositories/VetsInTech/Python Fundamentals/1121-itp/itp_week_3/day_4/rickandmorty.xlsx")