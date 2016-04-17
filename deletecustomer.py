import sys
import dwollaswagger
import requests
import json

oauthToken = sys.argv[1]

url = 'https://api.dwolla.com/customers/' + sys.argv[2]
headers = {'Accept': 'application/vnd.dwolla.v1.hal+json',
           'Authorization': 'Bearer' + oauthToken}
r = requests.delete(url, headers=headers)
parsed_json = json.loads(r.text)
print parsed_json