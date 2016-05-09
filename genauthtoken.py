import requests
import json
import sys
import time


def gentoken(inputtoken):
	url = 'https://uat.dwolla.com/oauth/v2/token'

	payload = {
	  "client_id": "KORB1uPLiCs2vO96B4Hiwxf8PsQ3Vk43I4k4oopegs5HjrmkLd",
	  "client_secret": "6919gTg6EcX1EK2YulRvDgWeDuMTvIFUt3krwux52e4REeP7Mq",
	  "refresh_token": inputtoken,
	  "grant_type": "refresh_token"
	}

	new_tok = requests.post(url, data=payload)
	parsed_json = json.loads(new_tok.text)
	refreshtoken = parsed_json['refresh_token']
	accesstoken = parsed_json['access_token']
	print refreshtoken
	print accesstoken

	time.sleep(3000)
	gentoken(refreshtoken)

gentoken(sys.argv[1])