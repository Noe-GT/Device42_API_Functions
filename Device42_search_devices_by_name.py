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

def get_device_by_name(name, token):
    url = f"{base_url}/api/1.0/devices/name/{name}/"
    headers = {'Authorization' : f'Bearer {token}',}
    response = requests.get(url,  verify=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"error {response.status_code}")

token = get_identification_token()
device = get_device_by_name('device_name', token) #change the device name
print(device)
