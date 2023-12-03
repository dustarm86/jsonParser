import requests
import json

# JSON data example to parse
clothingJsonExample = '''
[
    {
      "id": 10,
      "name": "shirt",
      "color": "red",
      "price": "$123"
    },
    {
      "id": 11,
      "name": "coat",
      "color": "black",
      "price": "$2300"
    }
]
'''

# Parse the JSON example
parsed_data = json.loads(clothingJsonExample)

for item in parsed_data:
    item_id = item['id']
    item_name = item['name']
    item_color = item['color']
    item_price = item['price']

    # Print the JSON details of each item
    print(f"Item ID: {item_id}")
    print(f"Name: {item_name}")
    print(f"Color: {item_color}")
    print(f"Price: {item_price}")
    print()