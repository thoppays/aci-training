import requests

url = "http://192.168.10.90/nuova"

payload = "<configConfMos\ncookie=\"1541770397/0e537936-565e-4fb8-b4ce-a0c15fcfdc8c\"\ninHierarchical=\"false\">\n    <inConfigs>\n<pair key=\"org-root/org-PythonMaster\">\n    <orgOrg\n    name=\"PythonMaster\"\n    dn=\"org-root/org-PythonMaster\"\n    \n    status=\"created\"\n    \n    sacl=\"addchild,del,mod\">\n    </orgOrg>\n</pair>\n    </inConfigs>\n</configConfMos>\n"
headers = {
    'Content-Type': "text/xml",
    'Authorization': "Basic Y2lzY286Y2lzY28="
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
