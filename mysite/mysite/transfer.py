'''
Author: Peter Chen
Adapted from: https://docsv2.dwolla.com/#transfers
Purpose: Creates a Transfer from two sources. Please check the Readme for more details.
'''
import sys
import dwollaswagger

def maketrans(token, source, dest, value):
    oauthToken = sys.argv[1]
    dwollaswagger.configuration.access_token = oauthToken
    client = dwollaswagger.ApiClient('https://api-uat.dwolla.com')
    transfers_api = dwollaswagger.TransfersApi(client)
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

    return xfer



