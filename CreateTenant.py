import requests

url = "http://192.168.10.1/api/node/mo/uni/tn-testtenant.json"
cookie = {"APIC-cookie": "TUq0BXAftVIR5wnRavZ0G/7//D5Jit4QYRUC+78o/bGaKgBuuCN/6SBLmFe0h5k12pB1HC3rgObBonE5ByFhJ8vtROje85690fWsVVKq/lO3exh7YNW9acFuhZDoGthu3a18M6SqO6kwvaXJ/eXBVoKDfnSFiZYWjOC3+dAKzy0="}

payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-testtenant\",\r\n\t\t\t\"name\": \"testtenant\",\r\n\t\t\t\"rn\": \"tn-testtenant\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
response = requests.request("POST", url, data=payload, cookies=cookie)

print(response.text)