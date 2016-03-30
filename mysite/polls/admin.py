from django.contrib import admin

# Register your models here.

from polls.models import Pet
admin.site.register(Pet)
