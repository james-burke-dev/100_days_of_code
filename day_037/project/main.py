import requests 
from datetime import date 

PIXELA_BASE_URL = "https://pixe.la/v1/users"

USERNAME = "renzl0r"
TOKEN = "uuuuhhhaas"

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

response = requests.post(url=PIXELA_BASE_URL, json=user_params)

print(response.text)

graph_params = {
    "id": "a1b2c3d4",
    "name": "habit",
    "unit": "minutes",
    "type": "int",
    "color": "ichou",

}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"{PIXELA_BASE_URL}/{user_params["username"]}/graphs"

graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

print(graph_response.text)

today = date.today()
formatted_today = today.strftime("%Y%m%d")

pixel_params = {
    "date": formatted_today,
    "quantity": 1
}

pixel_endpoint = f"{PIXELA_BASE_URL}/{user_params["username"]}/graphs/{graph_params["id"]}"

pixel_response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)

print(pixel_response)