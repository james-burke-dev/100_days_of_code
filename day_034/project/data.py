import requests

TRIVA_API_URL = "https://opentdb.com/api.php"
params = {"amount": 10,
          "type": "boolean"}

response_json = requests.get(url=TRIVA_API_URL, params=params).json()

question_data = response_json["results"]

