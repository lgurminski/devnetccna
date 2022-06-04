import requests
import json
import time

def getToken():
    req = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"
    Headers = {'Authorization' : 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='}
    resp = requests.post(req, verify = False, headers=Headers)
    return resp.json()["Token"],resp.status_code


def getNetworkDevices(token):
    req = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"
    Headers = {'Content-type': 'application/json','Accept': 'application/json','X-Auth-Token': token }
    resp = requests.get(req, verify=False, headers=Headers)
    file = open("cisco_dna_devices_result.txt", 'w')
    json.dump(resp.json(),file,indent = 4)
    return resp.status_code

def getClientHealth(token):
    req = "https://sandboxdnac.cisco.com/dna/intent/api/v1/client-health?timestamp"+str(int(time.time()))
    Headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'X-Auth-Token': token}
    resp = requests.get(req, verify=False, headers=Headers)
    file = open("cisco_dna_health_result.txt", 'w')
    json.dump(resp.json(),file,indent = 4)
    return resp.status_code

getNetworkDevices(getToken()[0])
getClientHealth(getToken()[0])

