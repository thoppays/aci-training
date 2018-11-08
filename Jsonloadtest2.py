import json
json_string = '{"aaaUser": {"attributes": {"name": "admin", "pwd": "cisco"} } }'
parsed_json = json.loads(json_string)
print(parsed_json['aaaUser']['attributes']['name'])
