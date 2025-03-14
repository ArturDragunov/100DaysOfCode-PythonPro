#%%
import requests
from datetime import datetime
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()
USERNAME = "arturdragunov98"
TOKEN = os.getenv('PIXELA_TOKEN')
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# ## POST - we are sending information to the database to create a user: https://pixe.la/@arturdragunov98
# COMMENT OUT BEFORE RUNNING. THEN COMMENT BACK
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Read Page",
    "unit": "pages",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN 
    # this is more secure approach instead of adding API KEY directly into parameters!!
    # your url won't consist of token as it will be encrypted
}

# COMMENT OUT BEFORE RUNNING. THEN COMMENT BACK
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text) # we created https://pixe.la/v1/users/arturdragunov98/graphs/graph1.html

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"), # %Y-%m-%d would give output 2024-05-24
    "quantity": input("How many pages have you read today?"),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4"
}

## PUT -> UPDATE existing piece of data
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


## DELETE -> DELETE existing piece of data
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)









