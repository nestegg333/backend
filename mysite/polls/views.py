from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, permissions
from polls.models import Owner, Payment, Pet
from django.contrib.auth.models import User
from polls.serializers import UserSerializer, OwnerSerializer, PaymentSerializer, PetSerializer, TokenSerializer
from djoser.views import LoginView, RegistrationView
from django.contrib.auth import get_user_model, user_logged_in, user_logged_out
from rest_framework import generics, permissions, status, response, views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.tokens import default_token_generator
from djoser import signals, settings
from mysite import genauthtoken, customergen, addbank, verifybank, transfer
import json

# Create your views here.
def index(request):
    return HttpResponse("Welcome to NestEgg.")


@csrf_exempt
def owners_list(request):
    """
    List all owners, or create a new owner.
    """
    if request.method == 'GET':
        owners = Owner.objects.all()
        serializer = OwnerSerializer(owners, many=True, context={'request': request})
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OwnerSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def owner_detail(request, pk):
    """
    Retrieve, update or delete an owner.
    """
    try:
        owner = Owner.objects.get(pk=pk)
    except Owner.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OwnerSerializer(owner, context={'request': request})
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OwnerSerializer(owner, data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        owner.delete()
        return HttpResponse(status=204)


@csrf_exempt
def pets_list(request):
    """
    List all owners, or create a new pet.
    """
    if request.method == 'GET':
        pets = Pet.objects.all()
        serializer = PetSerializer(pets, many=True, context={'request': request})
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PetSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def pet_detail(request, pk):
    """
    Retrieve, update or delete a pet.
    """
    try:
        pet = Pet.objects.get(pk=pk)
    except Pet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PetSerializer(pet, context={'request': request})
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PetSerializer(pet, data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pet.delete()
        return HttpResponse(status=204)

@csrf_exempt
def owner_payment_list(request, pk):
    """
    Retrieve all payments associated with user or make a payment. 
    """

    if request.method == 'GET':
        payments = Payment.objects.all().filter(owner=pk)
        serializer = PaymentSerializer(payments, many=True, context={'request': request})
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        payment = Payment.objects.create(owner=pk)
        owner = Owner.objects.get(pk=pk)
        owner.update(numTrans=F('numTrans')+1)
        data = JSONParser().parse(request)
        serializer = PaymentSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            payment = serializer.data
            # make actual transfer on dwolla
            token = genauthtoken.genToken()
            transitionaccount = 'https://api-uat.dwolla.com/funding-sources/3b0ab312-d24a-4ade-adc3-abe35ef3383b'
            trans1 = transfer.maketrans(token, owner.checkSource, transitionaccount, str(payment.amount))
            trans2 = transfer.maketrans(token, transitionaccount, owner.saveSource, str(payment.amount))
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class CustomLoginView(LoginView):
    """
    Custom login that returns both the token and the user
    """
    # original Djoser LoginView
    # https://github.com/sunscrapers/djoser/blob/master/djoser/views.py
    def action(self, serializer):
        user = serializer.user
        token, _ = Token.objects.get_or_create(user=user)
        user_logged_in.send(sender=user.__class__, request=self.request, user=user)
        return Response(
            data=TokenSerializer(token, context={'request': self.request}).data,
            status=status.HTTP_200_OK,
        )
class CustomRegistrationView(RegistrationView):
    """
    Custom registration that creates a user on NestEgg and on Dwolla
    """
    def perform_create(self, serializer):
        user = serializer.validated_data
        # if no email is entered, an email is generated from the username for the purposes of creating a Dwolla account
        if (user['email'] == ""):
            email = str(user['username']) + '@gmail.com'
        else:
            email = str(user['email'])
        instance = serializer.save()
        user = serializer.data
        user = User.objects.get(id=user['id'])
        owner = user.owner
        checkNum = str(owner.checkNum)
        saveNum = str(owner.saveNum)
        routeNum = str(owner.routeNum)
        signals.user_registered.send(sender=self.__class__, user=instance, request=self.request)
        # gets a token
        token = genauthtoken.genToken()
        # makes a customer on Dwolla
        customer = customergen.makeCust(token, "test", "test2", email, str(owner.address), str(owner.city), str(owner.state), str(owner.postalcode), str(owner.dob), str(owner.ssn), str(owner.phone))
        # send bank account info to Dwolla
        checkbank = addbank.makeBank(token, customer, routeNum, checkNum, str(user.username))
        savebank = addbank.makeBank(token, customer, routeNum, saveNum, str(user.username))
        verifybank.verify(token, checkbank)
        verifybank.verify(token, savebank)
        owner.custDwolla = customer
        owner.checkSource = checkbank
        owner.saveSource = savebank
        owner.save()
        if settings.get('SEND_ACTIVATION_EMAIL'):
            self.send_email(**self.get_send_email_kwargs(instance))

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Owner table
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Payment table
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PetViewSet(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Pet table
    queryset = Pet.objects.all()
    serializer_class = PetSerializer