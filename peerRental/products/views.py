from django.shortcuts import render,redirect
from products.forms import *
from products.models import *
from userAuthenticate.models import *

def upload_prod(req):
    forms = ProductFrom()
    if req.method == 'POST':
        forms = ProductFrom(req.POST,req.FILES)
        if forms.is_valid():
            # prod_img = req.FILES.getlist('prod_img')
            # description = req.POST.get('description')
            # price = req.POST.get('price')
            # rent_type = req.POST.get('rent_type')
            # title = req.POST.get('title')
            # Products.objects.create(
            #     product_image=prod_img,
            #     description = description,
            #     price=price,
            #     rent_type=rent_type,
            #     title=title
            # )
            user = CustomUser.objects.filter(email=req.user).values().first()
            print(user)
            return redirect(f"/user/{user['id']}")
    return render(req,'productinsert.html',context={
        'forms':forms
    })
