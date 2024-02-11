import requests
from pprint import pprint
import json

response = requests.get("https://opentdb.com/api_category.php")
# pprint(response.json())

with open("categories.json", "w") as file:
    json.dump(response.json(), file, indent=4)