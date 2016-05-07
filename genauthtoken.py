import requests
import json
import sys

#refresh token YkGO975Bcttuxq5xm4tuhYelJwBfIyhjquGkDIsqcsq20f3yxP

url = 'https://uat.dwolla.com/oauth/v2/token'

payload = {
  "client_id": "KORB1uPLiCs2vO96B4Hiwxf8PsQ3Vk43I4k4oopegs5HjrmkLd",
  "client_secret": "6919gTg6EcX1EK2YulRvDgWeDuMTvIFUt3krwux52e4REeP7Mq",
  "refresh_token": sys.argv[1],
  "grant_type": "refresh_token"
}

new_tok = requests.post(url, data=payload)
parsed_json = json.loads(new_tok.text)
# print parsed_json['refresh_token']
print parsed_json['access_token']



# client_id = 'KORB1uPLiCs2vO96B4Hiwxf8PsQ3Vk43I4k4oopegs5HjrmkLd'
# redirect_uri = 'https://tokengenerator.dwolla.com/redirect'
# scope = 'send|transactions|funding|managecustomers'

# url = 'https://uat.dwolla.com/oauth/v2/authenticate?client_id=' + client_id + '&response_type=code&redirect_uri=' + redirect_uri + '&scope=' + scope

# # payload = {
# #   "client_id": "KORB1uPLiCs2vO96B4Hiwxf8PsQ3Vk43I4k4oopegs5HjrmkLd",
# #   "client_secret": "6919gTg6EcX1EK2YulRvDgWeDuMTvIFUt3krwux52e4REeP7Mq",
# #   "grant_type": "client_credentials"
# # }

# new_tok = requests.post(url)