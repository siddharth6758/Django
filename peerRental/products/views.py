from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from products.forms import *
from products.models import *
from userAuthenticate.models import *


@login_required(login_url='/login/')
def upload_prod(req):
    forms = ProductFrom()
    if req.method == 'POST':
        forms = ProductFrom(req.POST,req.FILES)
        if forms.is_valid():
            # prod_img = req.FILES.get('prod_img')
            # description = req.POST.get('description')
            # price = req.POST.get('price')
            # rent_type = req.POST.get('rent_type')
            # title = req.POST.get('title')
            # Products.objects.create(
            #     posted_by=req.user,
            #     product_image=prod_img,
            #     description = description,
            #     price=price,
            #     rent_type=rent_type,
            #     title=title
            # )
            product = forms.save(commit=False)
            product.posted_by_id = req.user.id
            forms.save()
            return redirect(f"/user/{req.user.id}")
        else:
            print(forms.error)
    return render(req,'productinsert.html',context={
        'forms':forms,
        'id':req.user.id,
    })
