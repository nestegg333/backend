from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField

class Pet(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()
    def _str_(self):
    	return self.name


class Owner(models.Model):

	# determines the base cost of interactions based on the savings goal
	@property
	def baseCost(self):
		goal = self.goal * 100
		days = 30

		vFactor = 10
		tFactor = 3
		fFactor = 1

		vet = 1
		toy = 4
		food = days - vet - toy

		factor = (food * fFactor + toy * tFactor + vet * vFactor)
		remainder = goal % factor
		baseCost = (goal - remainder) / factor

		# The returned value is the amount * 100, so that there are never any issues with double/float rounding
		# e.g., $2.12 -> 212
		return baseCost

	# determines the random interaction order of the month
	@property
	def interactionOrder(self):
		import random 
		order = 'F' * 25
		order = order + 'T' * 4
		order = order + 'V'
		return ''.join(random.sample(order, len(order)))

	user = AutoOneToOneField(User, on_delete=models.CASCADE)
	pet = AutoOneToOneField(Pet, on_delete=models.CASCADE, null=True)
	numPets = models.PositiveIntegerField(default=1)
	goal = models.PositiveIntegerField(default=100)
	progress = models.IntegerField(default=0)
	checkNum = models.PositiveIntegerField(default=0)
	saveNum =models.PositiveIntegerField(default=0)
	_interactionOrder = property(interactionOrder)
	_baseCost = property(baseCost)
	numTrans = models.PositiveIntegerField(default=0)
	lastPay = models.CharField(max_length=30, blank=True, null=True)
	address = models.CharField(max_length=100, default="123 Test")
	city = models.CharField(max_length=100, default="Princeton")
	state = models.CharField(max_length=100, default="NJ")
	postalcode = models.CharField(max_length=5, default="08544")
	dob = models.CharField(max_length=10, default="1995-01-01")
	ssn = models.CharField(max_length=15, default="1234")
	phone = models.CharField(max_length=15, default="1234567890") 


class Payment(models.Model):
	owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
	date = models.DateField(auto_now_add=True)
	amount = models.PositiveIntegerField()


