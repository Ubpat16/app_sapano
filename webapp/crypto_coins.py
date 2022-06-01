import requests
import json

URL = "https://api.livecoinwatch.com/coins/list"

payload = json.dumps({
    "currency": "USDT",
    "sort": "rank",
    "order": "ascending",
    "offset": 0,
    "limit": 10,
    "meta": False
})
headers = {
    'content-type': 'application/json',
    'x-api-key': '1546b383-e1b3-4419-ac14-e4052ccde6bf'
}

response = requests.request("POST", URL, headers=headers, data=payload)
