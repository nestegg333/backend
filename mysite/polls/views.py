from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework import permissions
from polls.models import Owner
from polls.models import Payment
from polls.models import Pet
from django.contrib.auth.models import User
from polls.serializers import UserSerializer
from polls.serializers import OwnerSerializer
from polls.serializers import PaymentSerializer
from polls.serializers import PetSerializer
from polls.serializers import TokenSerializer
from djoser.views import LoginView
from djoser.views import RegistrationView
from django.contrib.auth import get_user_model, user_logged_in, user_logged_out
from rest_framework import generics, permissions, status, response, views
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.tokens import default_token_generator
from djoser import signals, settings
from mysite import genauthtoken, customergen

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
    def action(self, serializer):
        user = serializer.user
        token, _ = Token.objects.get_or_create(user=user)
        user_logged_in.send(sender=user.__class__, request=self.request, user=user)
        return Response(
            data=TokenSerializer(token, context={'request': self.request}).data,
            status=status.HTTP_200_OK,
        )
class CustomRegistrationView(RegistrationView):
    ## how to create users using Djoser 
    # original Djoser RegistrationView
    # https://github.com/sunscrapers/djoser/blob/master/djoser/views.py
    def perform_create(self, serializer):
        instance = serializer.save()
        signals.user_registered.send(sender=self.__class__, user=instance, request=self.request)
        # gets a token
        token = genauthtoken.genToken()
        # need to somehow get the user that was just created
        customer = customergen.makeCust(token,"peter", "chen", "pcchen@princeton.edu", "1234 rolling hills dr", "morgantown", "wv", "26508", "1994-01-01", "1234", "5555555555")
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