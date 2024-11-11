#    ███╗   ██╗ ██████╗    \
#    ████╗  ██║██╔════╝     \      Made by : Noe Gebert
#    ██╔██╗ ██║██║  ███╗     \
#    ██║╚██╗██║██║   ██║     /
#    ██║ ╚████║╚██████╔╝    /      Made on : 16/08/2024
#    ╚═╝  ╚═══╝ ╚═════╝    /

import requests
import urllib3
# uncomment next for basic auth
#from requests.auth import HTTPBasicAuth

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #avoids warnings

base_url = "your URL"
client_key = "Your client key"
client_secret = "your secret"

device_name_list = ["mydevice", "mydevice2"] #Change the device list to match the one your looking to test
return_data = "id" #change to return specific data like : os, type, ..

def get_identification_token():
# Make the POST request to get the token
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
        return 84

token = get_identification_token()

for device_name in device_name_list:
    data = get_device_by_name(device_name, token)
    if data == 84:
        output = "Incorect device name"
    else:
        if data[f"{return_data}"] == "":
            output = f"no {return_data}"
        else:
            output = data[f"{return_data}"]
    print(f"{device_name} : {output}")
