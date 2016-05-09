import requests
import json
import sys
import time


<<<<<<< HEAD:genauthtoken.py
def gentoken():
	frefresh = open('refresh_token.txt', 'r')
	inputtoken = frefresh.read()
	print inputtoken
=======
def genToken():
>>>>>>> 299c7dd7ca1fc4f344bd1a8628420062b6991698:mysite/mysite/genauthtoken.py
	url = 'https://uat.dwolla.com/oauth/v2/token'

	payload = {
	  "client_id": "KORB1uPLiCs2vO96B4Hiwxf8PsQ3Vk43I4k4oopegs5HjrmkLd",
	  "client_secret": "6919gTg6EcX1EK2YulRvDgWeDuMTvIFUt3krwux52e4REeP7Mq",
	  "refresh_token": "4jg4SaM6QdXJbN3TUyCGPqgnTnozCHwx7NLfjPux4dDXlSSUhi",
	  "grant_type": "refresh_token"
	}

	new_tok = requests.post(url, data=payload)
	parsed_json = json.loads(new_tok.text)
<<<<<<< HEAD:genauthtoken.py
	newRefresh = parsed_json['refresh_token']
	newAccess = parsed_json['access_token']

	frefresh = open('refresh_token.txt', 'w+')
	faccess = open('access_token.txt', 'w+')
	faccess.write(newAccess)
	frefresh.write(newRefresh)

gentoken()
=======
	return parsed_json['refresh_token']
gentoken(sys.argv[1])
>>>>>>> 299c7dd7ca1fc4f344bd1a8628420062b6991698:mysite/mysite/genauthtoken.py
