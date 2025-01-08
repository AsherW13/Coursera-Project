from django.contrib import admin

# Register your models here.
from .models import Menu, Booking
from rest_framework.authtoken.models import Token

admin.site.register(Menu)
admin.site.register(Booking)
admin.site.register(Token)