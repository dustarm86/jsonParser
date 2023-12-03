import json

# example JSON
#cityResidents = '{"name": "Steve French", "age": 32, "city": "Florida"}, {"name": "Bob Vance", "age": 21, "city": "Maine"}' #, '{"name": "Bob Vance", "age": 21, "city": "Maine"}'
cityResidents = '{"name": "Steve French", "age": 32, "city": "Florida"}'

# convert JSON to an object to be parsed
cityResidentsObject = json.loads(cityResidents)

# prints the value of the key you chose from the JSON
print(cityResidentsObject["city"])
