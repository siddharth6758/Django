from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from products.forms import *
from products.models import *
from userAuthenticate.models import *
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
            product.save()
            return redirect(f"/user/{req.user.id}")
        else:
            print(forms.error)
    return render(req,'productinsert.html',context={
        'forms':forms,
        'id':req.user.id,
    })


@login_required(login_url='/login/')
def edit_prod(req,prod_id,id):
    product = Products.objects.filter(prod_id=prod_id).filter(posted_by_id=id).first()
    forms = ProductFrom(instance=product)
    if req.method == 'POST':
        print('inside method')
        forms = ProductFrom(req.POST,req.FILES,instance=product)
        if forms.is_valid():
            prod_img = req.FILES.get('product-image')
            description = req.POST.get('description')
            price = req.POST.get('price')
            rent_type = req.POST.get('rent_type')
            title = req.POST.get('title')
            if prod_img:
                product.product_image - prod_img
            product.title = title
            product.description = description
            product.price = price
            product.rent_type = rent_type
            product.save()
            return redirect(f'/user/{id}')
    return render(req,'productedit.html',context={
        'forms':forms,
        'product':product,
        'id':req.user.id,
    })


@login_required(login_url='/login/')
def chatwith(req,prod_id,id):
    messages = list(ChatMessages.objects.filter(chat_prod_id=prod_id).filter(msg_to=id).values())
    unique_chats = {i['msg_from'] for i in messages}
    chat_users = []
    for i in unique_chats:
        user_info = {}
        user_info['id'] = i
        user_info['username'] = CustomUser.objects.filter(id=i).values().first()['username']
        user_info['email'] = CustomUser.objects.filter(id=i).values().first()['email']
        user_info['last_chat'] = ChatMessages.objects.filter(chat_prod_id=prod_id).filter(msg_from=i).values().last()['message']
        chat_users.append(user_info)
    return render(req,'chatwith.html',context={
        'id':id,
        'prod_id':prod_id,
        'userchatdetails':chat_users,
    })