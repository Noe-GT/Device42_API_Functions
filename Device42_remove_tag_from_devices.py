#    ███╗   ██╗ ██████╗    \
#    ████╗  ██║██╔════╝     \      Made by : Noe Gebert
#    ██╔██╗ ██║██║  ███╗     \
#    ██║╚██╗██║██║   ██║     /
#    ██║ ╚████║╚██████╔╝    /      Made on : 19/08/2024
#    ╚═╝  ╚═══╝ ╚═════╝    /

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #avoids warnings

base_url = "your URL"
client_key = "Your client key"
client_secret = "your secret"

device_name_list = ["mydevice1", "mydevice2"] #Replace the device names with yours

# Make the POST request to get the token
def get_identification_token():
    token_url = f'{base_url}/tauth/1.0/token/'
    response = requests.post(token_url, auth=(client_key, client_secret), verify=False)
    if response.status_code == 200:
        token = response.json().get('token')
        return token
    else:
        print(f"Failed to get token: {response.status_code} - {response.text}")

def remove_device_tag(token, device_name, tag_to_remove):
    """ Remove a tag from a device.
    :param token: Base64 encoded authorization token
    :param device_name: Name of the device
    :param tag_to_remove: Tag to remove from the device
    :return: Response from the API
    """
    url = f'{base_url}/api/1.0/device/'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'Authorization' : f'Bearer {token}'
    }
    data = {
        'name': device_name,
        'tags_remove': tag_to_remove
    }
    response = requests.post(url, headers=headers, data=data, verify=False)
    if response.status_code == 200:
        return 'Tag removed successfully.'
    return 'Failed to remove tag'

token = get_identification_token()
tag_to_remove = 'your_tag' #Change to match the tag you want to remove

for device_name in device_name_list:
    output = remove_device_tag(token, device_name, tag_to_remove)
    print(f"{device_name} : {output}")
