import sys
import dwollaswagger

if len(sys.argv) < 4:
    print "oauthtoken, source, dest, value"
    sys.exit()

oauthToken = sys.argv[1]
dwollaswagger.configuration.access_token = oauthToken
client = dwollaswagger.ApiClient('https://api-uat.dwolla.com')
transfers_api = dwollaswagger.TransfersApi(client)
source = sys.argv[2]
dest = sys.argv[3]
value = sys.argv[4]

def maketrans(source, dest, value):
    transfer_request = {
        "_links": {
            "source": {
                "href": source
            },
            "destination": {
                "href": dest
            }
        },
        "amount": {
            "currency": "USD",
            "value": value
        }
    }
    xfer = transfers_api.create(body=transfer_request)

    print xfer

# Jimmy - Checkings
#https://api-uat.dwolla.com/funding-sources/73a7d0d7-7038-4d72-825a-6a4555c921ab
#Jimmy - Savings
#https://api-uat.dwolla.com/funding-sources/6b9fae20-c394-4862-af5a-5c39078d30af
#Peter - Middle man
#https://api-uat.dwolla.com/funding-sources/3b0ab312-d24a-4ade-adc3-abe35ef3383b
#1 returned https://api-uat.dwolla.com/transfers/51c976cc-f704-e611-80df-0aa34a9b2388
maketrans(sys.argv[2], sys.argv[3], sys.argv[4])


