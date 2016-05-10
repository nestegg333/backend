'''
Author: Peter Chen
Adapted from: https://docsv2.dwolla.com/#create-a-customer-funding-source
Purpose: Adds bank account to Dwolla API. Please check the Readme for more details.
'''

import sys
import dwollaswagger

def makeBank(token, custid, routingnumber, accountnumber, nickname):
	oauthToken = token
	dwollaswagger.configuration.access_token = oauthToken
	client = dwollaswagger.ApiClient('https://api-uat.dwolla.com')
	funding_api = funding_api = dwollaswagger.FundingsourcesApi(client)
	new_fs = funding_api.create_customer_funding_source(custid, body = {
		"routingNumber": routingnumber,
	        "accountNumber": accountnumber,
	        "type": "checking",
	        "name": nickname})
	return new_fs


	