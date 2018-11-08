import requests

url = "http://192.168.10.80/restconf/api/config/native/ip/route"

payload = "{\r\n\t\"ned:route\": {\r\n\t\t\"ip-route-interface-forwarding-list\": [{\r\n\t\t\t\"prefix\": \"216.48.1.0\",\r\n\t\t\t\"mask\": \"255.255.255.0\",\r\n\t\t\t\"fwd-list\": [{\r\n\t\t\t\t\"fwd\": \"10.1.1.1\"\r\n\t\t\t}]\r\n\t\t}]\r\n\t}\r\n}"
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic YWRtaW46Y2lzY28="
    }

response = requests.request("PATCH", url, data=payload, headers=headers)

print(response.text)
print(response)