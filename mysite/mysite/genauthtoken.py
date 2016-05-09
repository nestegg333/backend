import requests
import json
import sys
import time


def genToken():
	url = 'https://uat.dwolla.com/oauth/v2/token'

	payload = {
	  "client_id": "KORB1uPLiCs2vO96B4Hiwxf8PsQ3Vk43I4k4oopegs5HjrmkLd",
	  "client_secret": "6919gTg6EcX1EK2YulRvDgWeDuMTvIFUt3krwux52e4REeP7Mq",
	  "refresh_token": "4jg4SaM6QdXJbN3TUyCGPqgnTnozCHwx7NLfjPux4dDXlSSUhi",
	  "grant_type": "refresh_token"
	}

	new_tok = requests.post(url, data=payload)
	parsed_json = json.loads(new_tok.text)
	return parsed_json['refresh_token']
gentoken(sys.argv[1])