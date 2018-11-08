import json
json_strng = '{"hi": "there"}'
parsed_json = json.loads(json_strng)
print(parsed_json['hi'])
