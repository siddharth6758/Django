from django.contrib import admin
from userAuthenticate.models import CustomUser
from products.models import Products
# Register your models here.

admin.register(CustomUser,Products)
