import requests
import json

oauthToken = 'yZOlWWyR0BRp4vsZZ7NcPLEVdwmnyKiAOmbUvYtcqtILywtVBR'

url = 'https://api-uat.dwolla.com/customers'
headers = {'Accept': 'application/vnd.dwolla.v1.hal+json',
           'Authorization': 'Bearer yZOlWWyR0BRp4vsZZ7NcPLEVdwmnyKiAOmbUvYtcqtILywtVBR'}
customers = requests.get(url, headers=headers)
parsed_json = json.loads(customers.text)
print parsed_json