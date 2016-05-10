'''
Author: Peter Chen
Adapted from: https://docsv2.dwolla.com/#create-a-customer-funding-source
Purpose: Adds bank account to Dwolla API. Please check the Readme for more details.
'''

import sys
import dwollaswagger

if len(sys.argv) < 5:
	print "oauthtoken, custid, routingnumber, accountnumber, nickname"
	sys.exit()

oauthToken = sys.argv[1]
dwollaswagger.configuration.access_token = oauthToken
client = dwollaswagger.ApiClient('https://api-uat.dwolla.com')
funding_api = funding_api = dwollaswagger.FundingsourcesApi(client)

def makeBank(custid, routingnumber, accountnumber, nickname):
	new_fs = funding_api.create_customer_funding_source(custid, body = {
		"routingNumber": routingnumber,
	        "accountNumber": accountnumber,
	        "type": "checking",
	        "name": nickname})
	print new_fs

try:
	fs = makeBank(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
except Exception, e:
	print e.body
	