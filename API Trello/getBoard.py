import requests
import json

url = "https://api.trello.com/1/boards/tUGoJi5t"

headers = {
   "Accept": "application/json"
}

query = {
   'key': '',
   'token': ''
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))