from django.contrib import admin
from userAuthenticate.models import CustomUser
from products.models import Products,ChatMessages,RentApplication
# Register your models here.

admin.site.unregister(CustomUser)

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','username','email')
    
@admin.register(ChatMessages)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('chat_prod_id','message','msg_to','msg_from')
@admin.register(RentApplication)
class RentApplicationAdmin(admin.ModelAdmin):
    list_display = ('applied_to_prod','application','buyer_id','seller_id','status')
