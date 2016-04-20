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
