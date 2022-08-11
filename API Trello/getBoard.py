import requests
import json

url = "https://api.trello.com/1/boards/tUGoJi5t"

headers = {
   "Accept": "application/json"
}

query = {
   'key': 'cfe4ed1398531251440d27a6bf998413',
   'token': '0d29b27acf985e03e0d8e8acf1138eb40ab1336db47a744622e3f1456d59c032'
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))