from django.contrib import admin
from userAuthenticate.models import CustomUser
from products.models import Products,ChatMessages,RentApplication
# Register your models here.

admin.register(CustomUser,Products,ChatMessages,RentApplication)
admin.site.register(ChatMessages)
admin.site.register(RentApplication)
