import requests
import json

oauthToken = 'yZOlWWyR0BRp4vsZZ7NcPLEVdwmnyKiAOmbUvYtcqtILywtVBR'

url = 'https://api.dwolla.com/funding-sources/6dc1e359-1655-4aa0-a4ab-345ad93f410e'
headers = {'Accept': 'application/vnd.dwolla.v1.hal+json',
           'Authorization': 'Bearer ' + oauthToken}
fund_source = requests.get(url, headers=headers)


deposit_url = "https://api-uat.dwolla.com//funding-sources/e52006c3-7560-4ff1-99d5-b0f3a6f4f909/micro-deposits"
headers = { 
	        'Authorization': 'Bearer ' + oauthToken,
	        'Content-Type': 'application/vnd.dwolla.v1.hal+json',
	        'Accept': 'application/vnd.dwolla.v1.hal+json', 
	        'Cache-Control': 'no-cache'      
            }

micro_deposit = requests.post(url, headers=headers)
print micro_deposit.text