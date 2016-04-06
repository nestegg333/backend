from django.http import HttpResponse
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

# Create your views here.
def index(request):
    return HttpResponse("Welcome to NestEgg.")

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Fish table
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Fish table
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PetViewSet(viewsets.ModelViewSet):
    # this fetches all the rows of data in the Fish table
    queryset = Pet.objects.all()
    serializer_class = PetSerializer