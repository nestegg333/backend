from polls.models import Owner
from polls.models import Payment
from polls.models import Pet
from django.contrib.auth.models import User

from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')

class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = ('name', 'created', 'active')

class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Owner
        user = UserSerializer()
        pet = PetSerializer()
        fields = ('user', 'pet', 'numPets', 'goal', 'progress', 'baseCost', 'numTrans', 'lastPay')

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        owner = OwnerSerializer()
        fields = ('owner', 'date', 'amount')
