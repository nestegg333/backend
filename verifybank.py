import sys
import dwollaswagger

oauthToken = sys.argv[1]
dwollaswagger.configuration.access_token = oauthToken
client = dwollaswagger.ApiClient('https://api-uat.dwolla.com')
funding_api = funding_api = dwollaswagger.FundingsourcesApi(client)

fs = sys.argv[2]
ret = funding_api.id(fs)
print ret.status

try:
	funding_api.micro_deposits(ret.id, body = {})

	x = funding_api.micro_deposits(ret.id, body = {
		"amount1": {
		"value": "0.03",
		"currency": "USD"
		},
		"amount2": {
		"value": "0.01",
		"currency": "USD"
		}
		})
except Exception, e:
	print fs
	print ret.status
	sys.exit(1)

print fs
print ret.status