import requests
import json

oauthToken = 'ePuTwtLSTKoJneHpTGmW294VhmSGdKw46gxvq0FKGMgUk8JrLO'

url = 'https://api-uat.dwolla.com/customers'
headers = {'Accept': 'application/vnd.dwolla.v1.hal+json',
           'Authorization': 'Bearer ePuTwtLSTKoJneHpTGmW294VhmSGdKw46gxvq0FKGMgUk8JrLO'}
customers = requests.get(url, headers=headers)
parsed_json = json.loads(customers.text)