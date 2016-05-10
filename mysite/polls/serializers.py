from polls.models import Owner, Payment, Pet
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from djoser import settings

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        owner = serializers.HyperlinkedRelatedField(view_name='owner', read_only=True)
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'owner')

class PetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'name', 'created', 'active')

class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Owner
        user = UserSerializer()
        pet = PetSerializer()
        fields = ('id', 'user', 'pet', 'numPets', 'goal', 'progress', 'checkNum', 'saveNum', 'routeNum', 'interactionOrder', 'baseCost', 'numTrans', 'lastPay', 'address', 'city', 'state', 'postalcode', 'dob', 'ssn', 'phone', 'custDwolla', 'checkSource', 'saveSource')

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        owner = OwnerSerializer()
        fields = ('id', 'owner', 'date', 'amount')

class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')
    user = UserSerializer()
    class Meta:
        model = Token
        fields = ('auth_token', 'user')


