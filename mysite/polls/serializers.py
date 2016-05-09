from polls.models import Owner
from polls.models import Payment
from polls.models import Pet
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers

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
        fields = ('id', 'user', 'pet', 'numPets', 'goal', 'progress', 'checkNum', 'saveNum', 'interactionOrder', 'baseCost', 'numTrans', 'lastPay')

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        owner = OwnerSerializer()
        fields = ('id', 'owner', 'date', 'amount')

class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')
    class Meta:
        model = Token
        user = UserSerializer()
        fields = ('auth_token', 'user')

