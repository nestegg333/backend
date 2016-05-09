# backend

## Progress to Date

### 3/30/16 (Xuewei)
* Set up sample Django backend and created SQLite table for model "Pet"

### 4/6/16 (Xuewei)
* Created models for Pet, Owner, and Payments and created SQLite tables for each model
* Set up Django REST API framework

### 4/13/16 (Xuewei)
* Added baseline cost calculation and interaction order determination to Owner model
* Incorporated "djoser" which provides set of basic views for authentication with Django REST framework
* Need to connect some parts to front-end to determine what else is missing on backend b/c a lot of backend functions are just updating the models and fields and altering the generic setter methods for each model

### 4/20/16 (Xuewei)
* GET, POST etc. requests to update owners, pets
* Make payment method (but still need to figure out how to set amount) that creates a new payment and updates the numTrans

### 4/20/16 (Peter)
Made authentication token refresher, customer creation, bank addition and verification, transfers between two bank accounts. 

## API

### Owners

#### POST /owners/
* Create a new owner

#### GET /owners/
* Get list of all owners

#### GET /owner/{pk}
* Retrieve an owner

#### PUT /owner/{pk}
* Update an owner

#### DELETE /owner/{pk}
* Delete an owner

### Pets

#### POST /pets/
* Create a new pet

#### GET /pets/
* Get list of all pets

#### GET /pet/{pk}
* Retrieve a pet

#### PUT /pet/{pk}
* Update a pet

#### DELETE /pet/{pk}
* Delete a pet

### Payments

#### GET /payments/{pk}
* Get list of all payments for an owner

#### POST /payments/{pk}
* Make a payment for the owner

## Dwolla API

## Get Access token
* Refreshes auth token from current refresh token provided by Dwolla SDK.
* Example:$ python genauthtoken.py 4jg4SaM6QdXJbN3TUyCGPqgnTnozCHwx7NLfjPux4dDXlSSUhi
* Output: xluHAUSRMqCDjtPeZbSSAAmvVvelpTYwIupxXb0SZYprDAZebF

## Add Customer
* Adds a customer given its oauthtoken, first, last, email, address, city, state, postalcode, dob, ssn, phonenum.  Returns an http response that has its customer id.
* For test input use fake data. email can be test, however no email can be used twice (dwolla does not support deleting emails yet). Address, city, and state each should be a single string (i.e. 1234-frist-center).  Postal code should be 5 digits.  Phone number must be 10 digits. 
* Example:$
* python customergen.py xluHAUSRMqCDjtPeZbSSAAmvVvelpTYwIupxXb0SZYprDAZebF John Smith js@test.com 1458-frist-center Princeton NJ 085 1994-01-01 1234 3046852269
* Output: https://api-uat.dwolla.com/customers/b8b16c93-63ef-4c2e-9cfb-12de65008bd9

## Add Bank
* Adds and verifies a bank.  Takes in oauthtoken, custid, routingnumber, accountnumber, nickname.   Returns an http response that has its bank id.
* Example:$ python addbank.py 1q3R6esMTHc3HqXkD2VFXNB8gHqDRc6XbupWaRZhJd2mWsla8n https://api-uat.dwolla.com/customers/ae4359df-c628-477b-8acc-140c785b1dcd 222222226 123456781 tests1
* Output: https://api-uat.dwolla.com/funding-sources/6e2a2153-be6f-4201-9f20-83ea06432ab1

## Verify Bank
* Verifies Bank info.  Take in oauthtoken and funding source.
* Example:$ python verifybank.py 1q3R6esMTHc3HqXkD2VFXNB8gHqDRc6XbupWaRZhJd2mWsla8n https://api-uat.dwolla.com/funding-sources/6e2a2153-be6f-4201-9f20-83ea06432ab1
* Output: https://api-uat.dwolla.com/funding-sources/6e2a2153-be6f-4201-9f20-83ea06432ab1

## Transfer
* Make a transfer between two bank accounts.  Takes in oauthtoken, source, dest, value.  Returns the transfer id of the transfer. Transition Bank Account('https://api-uat.dwolla.com/funding-sources/3b0ab312-d24a-4ade-adc3-abe35ef3383b')
* Example:$ python transfer.py 1q3R6esMTHc3HqXkD2VFXNB8gHqDRc6XbupWaRZhJd2mWsla8n https://api-uat.dwolla.com/funding-sources/3b0ab312-d24a-4ade-adc3-abe35ef3383b https://api-uat.dwolla.com/funding-sources/72056fd2-9bca-4524-bc2e-8bea0775480e 100
*Output:$ https://api-uat.dwolla.com/transfers/26655660-7114-e611-80e1-0aa34a9b2388



