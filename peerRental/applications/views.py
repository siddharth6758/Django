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
        vals['application'] = prodapplications.filter(buyer_id=id).first()['application']
        vals['prod_id'] = prod_id
        vals['status'] = prodapplications.filter(buyer_id=id).first()['status']
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
    product = Products.objects.filter(prod_id=prod_id,posted_by_id=req.user.id)
    if product:
        product.update(rented_by=buy_id)
    messages.success(req,'Product successfully rented!')
    return redirect(f'/myproducts/{req.user.id}')


@login_required(login_url='/login/')
def rejectapp(req,prod_id,buy_id):
    rentapp = RentApplication.objects.filter(applied_to_prod=prod_id,seller_id=req.user.id,buyer_id=buy_id)
    user = CustomUser.objects.filter(id=buy_id).first()
    if rentapp:
        rentapp.update(status='rejected')
    messages.info(req,f'{user.username} application rejected!')
    return redirect(f'/myproducts/{req.user.id}')


@login_required(login_url='/login/')
def myorders(req,id):
    applications = []
    sent_req = RentApplication.objects.filter(buyer_id=id).values('applied_to_prod_id','status')
    for i in sent_req:
        vals = {}
        prod = Products.objects.filter(prod_id=i['applied_to_prod_id']).first()
        vals['prod_id'] = i['applied_to_prod_id']
        vals['title'] = prod.title
        vals['image'] = prod.product_image
        vals['seller_username'] = prod.posted_by.username
        vals['seller_email'] = prod.posted_by.email
        vals['status'] = i['status']
        applications.append(vals)
    chats = ChatMessages.objects.filter(msg_from=id).values('chat_prod_id_id','msg_to')
    uni_prods = {i['chat_prod_id_id'] for i in chats}
    userchatdetails = []
    for prod in uni_prods:
        prod_sell = Products.objects.filter(prod_id=prod).first()
        chat_buyer = chats.filter(chat_prod_id=prod,msg_to=prod_sell.posted_by_id,msg_from=id).values('message').last()
        vals = {}
        vals['prod_id'] = prod
        vals['prod_title'] = prod_sell.title
        vals['seller_id'] = prod_sell.posted_by_id
        vals['seller_username'] = prod_sell.posted_by.username
        vals['seller_email'] = prod_sell.posted_by.email
        vals['last_chat'] = chat_buyer["message"]
        userchatdetails.append(vals)
    # print(userchatdetails)
    return render(req,'myorders.html',context={
        'id':req.user.id,
        'userchatdetails':userchatdetails,
        'applications':applications,
    })
    

@login_required(login_url='/login/')
def applicationedits(req,prod_id,buy_id):
    application = RentApplication.objects.filter(applied_to_prod=prod_id,buyer_id=buy_id).values('application').first()
    return render(req,'applicationedit.html',context={
        'id':req.user.id,
        'user':req.user,
        'application':application,
    })