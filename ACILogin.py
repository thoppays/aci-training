import requests

url = "http://192.168.10.1/api/aaaLogin.json"

payload = "{\r\n\t\"aaaUser\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"name\": \"admin\",\r\n\t\t\t\"pwd\": \"ciscoapic\"\r\n\t\t}\r\n\t}\r\n}"
response = requests.request("POST", url, data=payload)

print(response.text)