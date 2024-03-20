from django.db import models
from userAuthenticate.models import CustomUser
import random,string

RENT_CHOICES = (
    ('/hour','/hour'),
    ('/day','/day'),
    ('/week','/week'),
    ('/month','/month'),
    ('/year','/year'),
)

def pk_generator():
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=4))

class Products(models.Model):
    prod_id = models.CharField(max_length=4,primary_key=True)
    posted_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True) 
    product_image = models.FileField(upload_to='products/')
    description = models.CharField(max_length=200)
    price = models.CharField()
    rent_type = models.CharField(max_length=10,choices=RENT_CHOICES,default='/hour')
    title = models.CharField(max_length=20)
    
    def save(self,*args,**kwargs):
        if not self.prod_id:
            self.prod_id = pk_generator()
        super().save(*args, **kwargs)
        
class ChatMessages(models.Model):
    chat_over_prod = models.ForeignKey(Products,on_delete=models.CASCADE)
    buyer_id = models.CharField(max_length=2)    
    seller_id = models.CharField(max_length=2)
    date_time = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=200)    