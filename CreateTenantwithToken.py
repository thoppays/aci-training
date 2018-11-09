import requests
import json

url = "http://192.168.10.1/api/aaaLogin.json"

payload = "{\r\n\t\"aaaUser\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"name\": \"admin\",\r\n\t\t\t\"pwd\": \"ciscoapic\"\r\n\t\t}\r\n\t}\r\n}"
headers = {'Authorization': 'Basic YWRtaW46Y2lzY29hcGlj'}

response = requests.request("POST", url, data=payload, headers=headers)

#print(response.text)

json_response=json.loads(response.text)
tokenfromlogin=(json_response)['imdata'][0]['aaaLogin']['attributes']['token']

###

url = "http://192.168.10.1/api/node/mo/uni/tn-testtenant.json"
cookie = {"APIC-cookie": tokenfromlogin}

payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-testtenant\",\r\n\t\t\t\"name\": \"testtenant\",\r\n\t\t\t\"rn\": \"tn-testtenant\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)
