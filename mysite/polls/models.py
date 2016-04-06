from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()


class Owner(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	pet = models.OneToOneField(Pet, on_delete=models.CASCADE)
	numPets = models.PositiveIntegerField()
	goal = models.PositiveIntegerField()
	progress = models.IntegerField()
	#checkNum = 
	#saveNum =
	baseCost = models.IntegerField()
	numTrans = models.PositiveIntegerField()
	lastPay = models.DateField() 
	# need to retrieve Payment
	# what to do when user first initialized and no last payment?


class Payment(models.Model):
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
	date = models.DateField(auto_now_add=True)
	amount = models.PositiveIntegerField()


