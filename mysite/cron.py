'''
Author: Peter Chen
Adapted from https://github.com/kraiz/django-crontab
Purpose: Refreshes the refresh token every 30 minutes.
'''

import requests
import json
import sys
import time


def gentoken():
	frefresh = open('refresh_token.txt', 'r')
	inputtoken = frefresh.read()

	url = 'https://uat.dwolla.com/oauth/v2/token'

	payload = {
	  "client_id": "KORB1uPLiCs2vO96B4Hiwxf8PsQ3Vk43I4k4oopegs5HjrmkLd",
	  "client_secret": "6919gTg6EcX1EK2YulRvDgWeDuMTvIFUt3krwux52e4REeP7Mq",
	  "refresh_token": inputtoken,
	  "grant_type": "refresh_token"
	}

	new_tok = requests.post(url, data=payload)
	parsed_json = json.loads(new_tok.text)
	newRefresh = parsed_json['refresh_token']
	newAccess = parsed_json['access_token']
	
	frefresh = open('refresh_token.txt', 'w+')
	faccess = open('access_token.txt', 'w+')
	faccess.write(newAccess)
	frefresh.write(newRefresh)