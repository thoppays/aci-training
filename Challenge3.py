
#
# Generated ASA REST API sample script - Python 2.7
#

import base64
import json
import sys
import urllib2
# Uncomment the following two lines, if you are using Python 2.7.9 or above to connect to an ASA with a self-signed certificate.
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

server = "https://192.168.10.100"

username = "enable_1"
if len(sys.argv) > 1:
    username = sys.argv[1]
password = "cisco"
if len(sys.argv) > 2:
    password = sys.argv[2]


headers = {'Content-Type': 'application/json'}

api_path = "/api/objects/networkobjects"    # param
url = server + api_path
f = None

# POST OPERATION




post_data = {
  "host": {
    "kind": "IPv4Address",
    "value": "100.1.1.1"
  },
  "kind": "object#NetworkObj",
  "name": "Development",
  "objectId": "Development"
}
req = urllib2.Request(url, json.dumps(post_data), headers)
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
req.add_header("Authorization", "Basic %s" % base64string)
try:
    f  = urllib2.urlopen(req)
    status_code = f.getcode()
    print "Status code is "+str(status_code)
    if status_code == 201:
        print "Create was successful"
except urllib2.HTTPError, err:
    print "Error received from server. HTTP Status code :"+str(err.code)
    try:
        json_error = json.loads(err.read())
        if json_error:
            print json.dumps(json_error,sort_keys=True,indent=4, separators=(',', ': '))
    except ValueError:
        pass
finally:
    if f:  f.close()


###
import requests

"""
Modify these please
"""
url='http://192.168.10.60/ins'
switchuser='admin'
switchpassword='Passw0rd1'

myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_conf",
    "chunk": "0",
    "sid": "1",
    "input": "vlan 600 ;name Construction ;vlan 700 ;name Analysis",
    "output_format": "json"
  }
}
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

###


url = "http://192.168.10.80/restconf/api/config/native/ip/route"

payload = "{\r\n    \"ned:route\": {\r\n        \"ip-route-interface-forwarding-list\": [\r\n            {\r\n                \"prefix\": \"216.48.1.0\",\r\n                \"mask\": \"255.255.255.0\",\r\n                \"fwd-list\": [\r\n                    {\r\n                        \"fwd\": \"10.1.1.1\"\r\n                    }\r\n                ]\r\n            }\r\n\t\t],\r\n        \"static\": {}\r\n    }\r\n}"
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic YWRtaW46Y2lzY28="
    }

response = requests.request("PATCH", url, data=payload, headers=headers)

print(response.text)
print(response)
