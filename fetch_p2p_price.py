import requests
import os

headers = {'Authorization: Bearer' +  os.environ['API_KEY']}
query = {
  "filters": {
    "country": "BR"
  }
}
r = requests.get("https://hodlhodl.com/api/v1/offers", headers = headers, params=query)
response = requests.get()
print(response)
