from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from products.models import Products,RentApplication,ChatMessages
from userAuthenticate.models import CustomUser
from django.contrib import messages

@login_required(login_url='/login/')
def applicationsreq(req,prod_id,sell_id):
    prodapplications = RentApplication.objects.filter(applied_to_prod=prod_id,seller_id=sell_id).values()
    buyers = {i['buyer_id'] for i in prodapplications}
    applications = []
    for id in buyers:
        vals = {}
        buy_users = CustomUser.objects.filter(id=id).first()
        vals['buyer_id'] = buy_users.id
        vals['username'] = buy_users.username
        vals['email'] = buy_users.email
        vals['application'] = prodapplications.filter(applied_to_prod=prod_id,seller_id=sell_id,buyer_id=id).first()['application']
        vals['prod_id'] = prod_id
        applications.append(vals)
    return render(req,'productapplication.html',context={
        'id':req.user.id,
        'applications':applications
    })
    
@login_required(login_url='/login/')
def applicationdetails(req,prod_id,buy_id,sell_id):
    product = Products.objects.filter(prod_id=prod_id,posted_by_id=sell_id).first()
    application = RentApplication.objects.filter(applied_to_prod=prod_id,seller_id=sell_id,buyer_id=buy_id).first()
    user = CustomUser.objects.filter(id=buy_id).first()
    return render(req,'applicationdetails.html',context={
        'id':req.user.id,
        'product':product,
        'application':application,
        'user':user,
    })

@login_required(login_url='/login/')
def acceptapp(req,prod_id,buy_id):
    rentapp = RentApplication.objects.filter(applied_to_prod=prod_id,seller_id=req.user.id,buyer_id=buy_id).first()
    rentapp.status = 'accepted'
    rentapp.save()
    otherapp = RentApplication.objects.filter(applied_to_prod=prod_id,seller_id=req.user.id).exclude(buyer_id=buy_id)
    if otherapp:
        otherapp.update(status='rejected')
    return redirect(f'/myproducts/{req.user.id}')


@login_required(login_url='/login/')
def rejectapp(req,prod_id,buy_id):
    rentapp = RentApplication.objects.filter(applied_to_prod=prod_id,seller_id=req.user.id,buyer_id=buy_id).values()
    # rentapp.status = 'rejected'
    rentapp.save()
    return redirect(f'myproducts/{req.user.id}')