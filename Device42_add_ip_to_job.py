import requests, urllib3, sys, urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #avoids warnings

base_url = "your URL"
client_key = "Your client key"
client_secret = "your secret"

def get_identification_token():
    token_url = f'{base_url}/tauth/1.0/token/'
    response = requests.post(token_url, auth=(client_key, client_secret), verify=False)
    if response.status_code == 200:
        token = response.json().get('token')
        return token
    else:
        return None

def update_job(token, input_data):
    url = f'{base_url}/api/1.0/auto_discovery/vserver/'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'Authorization' : f'Bearer {token}'
    }
    response = requests.post(url, headers=headers, data=input_data, verify=False)
    if response.status_code == 200:
        return 0
    else:
        return 1

def get_jobs(token):
    url = f"{base_url}/api/1.0/auto_discovery/vserver/"
    headers = {'Authorization' : f'Bearer {token}',}
    response = requests.get(url,  verify=False, headers=headers)
    print(f"response code : {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def get_job_by_name(token, name):
    data = (get_jobs(token))
    count = 0
    if data:
        for job in data["jobs"]:
            count += 1
            if job["name"] == name:
                return job
    return None

def add_ip_to_job(token, add_ip, job_data):
    input_data = {
        'name': job_data["name"],
        'server': f'{job_data["servers"]},{add_ip}'
    }
    return update_job(token, input_data)

def runner(job_name, add_ip):
    token = get_identification_token()
    if not token:
        return f"Failed to get token."
    job_data = get_job_by_name(token, job_name)
    if not job_data:
        return f"ERROR : couldn't get job :  {job_name}."
    result = add_ip_to_job(token, add_ip, job_data)
    if result == 0:
        return 'job update successfull'
    return 'Failed to update job.'

def main():
    if len(sys.argv) != 3:
        return "Wrong number of arguments."
    job_name = sys.argv[1]
    add_ip = sys.argv[2]
    add_ip = add_ip.replace(' ', '')

    ip_list = add_ip.split(',')
    for ip in ip_list:
        if ip.count('.') != 3 or len(ip) > 15:
            return "Invalid IP/s"
        byte_list = ip.split('.')
        for byte in byte_list:
            if len(byte) < 1 or not byte.isdigit() or\
                int(byte) > 255 or len(byte) > 3:
                return "Invalid IP/s : incorrect byte"
    return runner(job_name, add_ip)

if __name__ == '__main__':
    print(main())

# DESCRIPTION :
# Adds given ip adresses to a given job

# USAGE :
# py Device42_add_ip_to_job.py <your job name> <ids_to_add>

# EXAMPLE :
# py Device42_add_ip_to_job.py my_device "10.10.10.10"
#   OR
# py Device42_add_ip_to_job.py my_device "10.10.10.10,33.33.33.33"

