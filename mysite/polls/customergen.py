import sys
import dwollaswagger
import requests

#if len(sys.argv) < 11:
#	print "oauthtoken, first, last, email, address, city, state, postalcode, dob, ssn, phonenum"
#	sys.exit()

def makeCust(oauthToken, first, last, email, address, city, state, postalcode, dob, ssn, phonenum):
    dwollaswagger.configuration.access_token = oauthToken
    client = dwollaswagger.ApiClient('https://api-uat.dwolla.com')
    customers_api = dwollaswagger.CustomersApi(client)
    new_customer = customers_api.create(body = {'firstName': first,
                                            'lastName': last,
                                            'email': email,
                                            'type': 'personal',
                                            'address1': address,
                                            'city': city,
                                            'state': state,
                                            'postalCode': postalcode,
                                            'dateOfBirth':  dob,

                                            # For the first attempt, only the
                                            # last 4 digits of SSN required

                                            # If the entire SSN is provided,
                                            # it will still be accepted
                                            'ssn': ssn,
                                            'phone': phonenum })
    return new_customer

#makeCust("peter", "chen", "pcchen@princeton.edu", "1234 rolling hills dr", "morgantown", "wv", "26508", "1994-01-01", "1234", "5555555555")

#A customer with the specified email already exists.
#try:
#    makeCust(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11])
#except Exception, e:
#   print e.body
#    sys.exit(1)
