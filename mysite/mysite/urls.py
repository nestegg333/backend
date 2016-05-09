"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from django.conf.urls import include
from polls import views

router = routers.DefaultRouter()
#makes sure that the API endpoints work
router.register(r'api/users', views.UserViewSet)
router.register(r'api/owners', views.OwnerViewSet)
router.register(r'api/payments', views.PaymentViewSet)
router.register(r'api/pets', views.PetViewSet)
admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^auth/login/$', views.CustomLoginView.as_view(), name='login'),
    url(r'^auth/register/$', views.CustomRegistrationView.as_view(), name='register'),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^auth/', include('djoser.urls')),
    url(r'^owners/$', views.owners_list),
    url(r'^owner/(?P<pk>[0-9]+)/$', views.owner_detail),
    url(r'^pets/$', views.pets_list),
    url(r'^pet/(?P<pk>[0-9]+)/$', views.pet_detail),
    url(r'^payments/(?P<pk>[0-9]+)/$', views.owner_payment_list),
]
