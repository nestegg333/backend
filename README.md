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
* Create a payment for an owner
