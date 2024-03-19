from django.db import models
from userAuthenticate.models import CustomUser
import random,string

def generate_filename(customuser,filename):
    return f'products/{customuser.user.username}/{filename}'

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
    posted_on = models.DateTimeField(auto_now=True) 
    product_image = models.FileField(upload_to=generate_filename)
    description = models.CharField(max_length=200)
    price = models.CharField()
    rent_type = models.CharField(max_length=10,choices=RENT_CHOICES,default='/hour')
    title = models.CharField(max_length=20)
    
    def save(self,*args,**kwargs):
        if not self.prod_id:
            self.prod_id = pk_generator()
        super().save(*args, **kwargs)