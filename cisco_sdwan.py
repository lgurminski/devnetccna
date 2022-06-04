import requests,json

user = "devnetuser"
password = "RG!_Yw919_83"
req = "https://sandbox-sdwan-1.cisco.com/j_security_check"

udata = {"j_username":user, "j_password":password}
Headers = {'Content-type': 'application/x-www-form-urlencoded'}

SESS = requests.session()
LOGIN_RESP = SESS.post(url=req, data=udata, verify=False)
print(LOGIN_RESP.status_code,LOGIN_RESP.cookies)

#GET TOKEN:
url = "https://sandbox-sdwan-1.cisco.com/dataservice/client/token"
TOKEN = SESS.get(url=url, verify=False)
print("TOKEN: ", TOKEN.content)

#GET DEVICES:
url="https://sandbox-sdwan-1.cisco.com/dataservice/device"
DEVICE_RESPONSE = SESS.get(url, verify = False)
DEVICE_ITEMS = json.loads(DEVICE_RESPONSE.content)['data']
file = open("cisco_sdwan_devices.txt",'w')
json.dump(DEVICE_ITEMS,file,indent=4)
file.close()

#GET TEMPLATES
url = "https://sandbox-sdwan-1.cisco.com/dataservice/template/device"
DEVICE_RESPONSE = SESS.get(url, verify = False)
TEMPLATES = json.loads(DEVICE_RESPONSE.content)['data']
file = open("cisco_sdwan_templates.txt",'w')
json.dump(TEMPLATES,file,indent=4)
file.close()
