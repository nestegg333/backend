from django.contrib import admin

# Register your models here.

from polls.models import Pet
admin.site.register(Pet)
from polls.models import Owner
admin.site.register(Owner)
from polls.models import Payment
admin.site.register(Payment)