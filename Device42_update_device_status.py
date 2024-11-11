#    ███╗   ██╗ ██████╗    \
#    ████╗  ██║██╔════╝     \      Made by : Noe Gebert
#    ██╔██╗ ██║██║  ███╗     \
#    ██║╚██╗██║██║   ██║     /
#    ██║ ╚████║╚██████╔╝    /      Made on : 02/08/2024
#    ╚═╝  ╚═══╝ ╚═════╝    /

import requests
import urllib3
#from requests.auth import HTTPBasicAuth -> remove comment for basic auth

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #avoids warnings

base_url = "your URL"
client_key = "Your client key"
client_secret = "your secret"
#if you don't have a client key, use basic authentification such as :
# auth=HTTPBasicAuth('user', 'password')

# Make the POST request to get the token
def get_identification_token():
    token_url = f'{base_url}/tauth/1.0/token/'
    response = requests.post(token_url, auth=(client_key, client_secret), verify=False)
    if response.status_code == 200:
        token = response.json().get('token')
        return token
    else:
        print(f"Failed to get token: {response.status_code} - {response.text}")

def update_device(id, token, input_data):
    url = f'{base_url}/api/2.0/devices/{id}/'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'Authorization' : f'Bearer {token}'
    }
    response = requests.put(url, headers=headers, data=input_data, verify=False)
    if response.status_code == 200:
        print('Device updated successfully!')
    else:
        print(f'Failed to update device. Status code: {response.status_code}')
        print('Response:', response.text)

token = get_identification_token()
id = 'your device id'  #change to the id of the device you wish to modify
input_data = {'tags': 'test_tag'} #Modify to change the value you wish to
update_device(id, token, input_data)
