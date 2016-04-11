import requests
import json


oauthToken = 'cDBT4jWISV0t7BXd4NiZ4WcRTkA8YPnycxhbJWXiWsxkkRAtky'

url = 'https://api-uat.dwolla.com/customers'
headers = {'Accept': 'application/vnd.dwolla.v1.hal+json',
           'Authorization': 'Bearer cDBT4jWISV0t7BXd4NiZ4WcRTkA8YPnycxhbJWXiWsxkkRAtky'}

def makeCust(first, last, email, address, city, state, postalcode, dob, ssn, phonenum):
	payload = {
	"firstName": first,
	"lastName": last,
	"email": email,
	"ipAddress": "",
	"type": "personal",
	"address1": address,
	"city": city,
	"state": state,
	"postalCode": postalcode,
	"dateOfBirth": dob,
	"ssn": ssn,
	"phone": phonenum
	}

	new_cust = requests.post(url, data=payload, headers=headers)
	parsed_json = json.loads(new_cust.text)
	print parsed_json

makeCust("peter", "chen", "pcchen@princeton.edu", "1234 rolling hills dr", "morgantown", "wv", "26508", "1994-01-01", "1234", "5555555555")