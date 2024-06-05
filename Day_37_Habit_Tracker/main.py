import requests

TOKEN = "1234567890"
USERNAME = "bikramsankhari"
GRAPH_ID = "abcd1234"
GRAPH_NAME = "newGraph"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_headers = {
    "X-USER-TOKEN": TOKEN,
}
graph_parameters = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": "hours",
    "type": "int",
    "color": "sora",
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=graph_headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_header = {
    "X-USER-TOKEN": TOKEN,
}
pixel_parameters = {
    "date": "20230426",
    "quantity": "5",
}

response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=pixel_header)
print(response.text)