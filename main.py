import requests
import json
USERNAME = "noyaq"
TOKEN = "This_not_a_secured_password!" # Not required to send env for password protection, free API
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
headers = {
    "X-USER-TOKEN": TOKEN
}

"""
##################################################
CREATE A ACCOUNT
##################################################

"""
# user_parameters = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }


# reponse = requests.post(url = PIXELA_ENDPOINT, json = user_parameters)
# print(reponse.text)

"""
##################################################
CREATE A GRAPH
##################################################
"""
# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
# graph_parameters = {
#     "id": "graph001",
#     "name": "Daily Walking Distance",
#     "unit": "steps",
#     "type": "float",
#     "color": "shibafu"
# }

# response = requests.post(url = graph_endpoint, json = graph_parameters, headers = headers)
# print(response.text)

"""
##################################################
POST A VALUE FOR A DAY
##################################################
The first day that entered data is 20240101
The second day that entered data is 20240108
"""

# value_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph001"

# value_parameters = {
#     "date": "20240108",
#     "quantity": "3544",
# }

# response = requests.post(url = value_endpoint, json = value_parameters, headers = headers)
# print(response.text)
"""
##################################################
PUT A VALUE FOR A DAY
##################################################
The 20240801 data is updated 
"""

# update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph001/20240108"

# update_parameters = {
#     "quantity": "13455",
# }

# response = requests.put(url = update_endpoint, json = update_parameters, headers = headers)
# print(response.text)