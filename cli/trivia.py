import requests
import json
from pprint import pprint

url = "https://opentdb.com/api.php?amount=50&category=18"
response = requests.get(url).json()
with open("trivia.json", "w") as file:
    json.dump(response, file, indent=4)