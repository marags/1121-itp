import json
import requests

r = requests.get("https://rickandmortyapi.com/api/character")
print(r.status_code)

print(r.text)

data = json.loads(r.text)
# print(data)
# print(type(r.text)) #string
# print(type(data))   #converts the json from string to dictionary


print(data['results'][2]['name']) #navigating/accessing the json object

#formatting json object
# print(json.dumps(data)) 
print(json.dumps(data, indent=4, sort_keys=True)) #JSON viewer/pretty print JSON object using indent