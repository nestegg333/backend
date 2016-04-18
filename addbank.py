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
	return new_fs

try:
	fs = makeBank(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
except:
	fund_sources = funding_api.get_customer_funding_sources(sys.argv[2])
	fs = str(fund_sources._embedded['funding-sources'][0]['_links']['self']['href'])

print fs
ret = funding_api.id(fs)

# x = funding_api.micro_deposits(ret.id, body = {
#   "amount1": {
#     "value": "0.03",
#     "currency": "USD"
#   },
#   "amount2": {
#     "value": "0.01",
#     "currency": "USD"
#   }
# })

# print ret.status

