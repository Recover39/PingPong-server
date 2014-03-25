import requests
import json

load = {"key1": "value1", "key2": "value2"}
print(load)
r = requests.post('http://127.0.0.1:5000/', data=json.dumps(load), headers={"Content-Type": "application/json"})
# print(r.status_code)
# print(r.text)
