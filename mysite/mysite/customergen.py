import sys
import dwollaswagger
import requests


def makeCust(token, first, last, email, address, city, state, postalcode, dob, ssn, phonenum):
    oauthToken = token
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
                                            'phone': phonenum})
    return new_customer



