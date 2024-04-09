from django.contrib import admin
from .models import CustomUser
# Register your models here.

admin.site.register(CustomUser)

class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','username','email']