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

maketrans(sys.argv[2], sys.argv[3], sys.argv[4])


