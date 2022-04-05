import requests
from datetime import datetime

USERNAME = "EyeHeartNickelback"
TOKEN = "LookAtThisPhotograph"
GRAPHID = "SomedaySomehow"

headers = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"

date = datetime.now()
today = date.strftime("%Y%m%d")


# parameters = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
#
# }

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_params = {
#     "id": GRAPHID,
#     "name": "Best Goddamn Band in the World",
#     "unit": "bpm",
#     "type": "float",
#     "color": "sora"
# }


# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
#
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
# update_params = {
#     "date": today,
#     "quantity": "1.5",
# }
#
# response = requests.post(url=update_endpoint, json=update_params, headers=headers)

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today}"
# update_params = {
#     "quantity": "2.2",
# }
#
# response = requests.put(url=update_endpoint, json=update_params, headers=headers)

# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today}"
# response = requests.delete(url=delete_endpoint, headers=headers)
