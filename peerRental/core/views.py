from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from userAuthenticate.models import CustomUser
from products.models import Products,ChatMessages,RentApplication
from django.contrib import messages
import re

empty_string_pattern = r'^\s*\S.*$'

def home(req):
    return render(req,'base.html')

@login_required    
def delete_prod(req,prod_id):
    user = Products.objects.filter(prod_id=prod_id).values().first()
    if user['posted_by_id'] == req.user.id:
        Products.objects.filter(prod_id=prod_id).delete()
        messages.success(req,'Product has been deleted successfully!')
        return redirect(f'/user')
    else:
        messages.error(req,'Could not delete product!')
        return redirect(f'/user')


@login_required(login_url='/login/')
def rent_prod(req,prod_id):
    buyuserid = req.user.id
    selluserid = Products.objects.filter(prod_id=prod_id).first()
    selluserid = selluserid.posted_by_id
    if buyuserid == selluserid:
        messages.info(req,'You cannot rent your own product!')
        return redirect(f'/user')
    return redirect(f'/rentprod/{prod_id}B{buyuserid}S{selluserid}')

@login_required(login_url='/login/')
def complete_order(req,prod_id,buy_id,sell_id):
    product = Products.objects.filter(prod_id=prod_id).first()
    if req.method == 'POST':
        chats = req.POST.get('chat-field')
        if not re.match(empty_string_pattern,chats):
            messages.info(req,'Chat cannot be empty or just spaces!')
        else:
            chat_save = ChatMessages.objects.create(
                chat_prod_id = product,
                msg_from = req.user.id,
                msg_to = sell_id,
                msg_type = 'going',
                message = chats
            )
            chat_save.save()
            return HttpResponseRedirect(reverse('complete_order', args=(prod_id, buy_id, sell_id)))
    chatmessages = ChatMessages.objects.filter(chat_prod_id=prod_id).filter(msg_from=buy_id).filter(msg_to=sell_id).values()
    applied_flag = 'false'
    if RentApplication.objects.filter(applied_to_prod=prod_id,buyer_id=buy_id).exists():
        applied_flag = 'true'
    return render(req,'rentpage.html',context={
        'id':buy_id,
        'product':product,
        'chatmessages':chatmessages,
        'applied_flag':applied_flag,
    })

@login_required(login_url='/login/')
def clearchats(req,prod_id,to_id,from_id):
    ChatMessages.objects.filter(chat_prod_id=prod_id).filter(msg_from=from_id).filter(msg_to=to_id).delete()
    if req.user.id == from_id:
        return redirect(f'/rentprod/{prod_id}B{from_id}S{to_id}')
    elif req.user.id == to_id:
        return redirect(f'/sellerchat/{prod_id}B{from_id}S{to_id}')


@login_required(login_url='/login/')
def myproducts(req,id):
    products = Products.objects.filter(posted_by_id=id)
    return render(req,'myproducts.html',context={
        'id':req.user.id,
        'products':products,
    })

@login_required(login_url='/login/')
def confirm_rent(req,prod_id,buy_id,sell_id):
    product = Products.objects.filter(prod_id=prod_id,posted_by_id=sell_id).first()
    if req.method == 'POST':
        application_msg = req.POST.get('application')
        if len(application_msg) == 0:
            messages.error(req,'Application cannot be Empty!')
            return redirect(f'/confirm_rent/{prod_id}B{buy_id}S{sell_id}')
        else:
            application = RentApplication.objects.create(
                applied_to_prod=product,
                buyer_id=buy_id,
                seller_id=sell_id,
                application=application_msg,
                status='pending'
            )
            application.save()
            messages.success(req,'Application sent to Seller!')
            return redirect(f'/user/{buy_id}')
    return render(req,'confirmrent.html',context={
        'id':req.user.id,
        'product':product,
    })

@login_required(login_url='/login/')
def sellerchat(req,prod_id,buy_id,sell_id):
    product = Products.objects.filter(prod_id=prod_id).first()
    buyer = CustomUser.objects.filter(id=buy_id).first()
    if req.method == 'POST':
        chats = req.POST.get('chat-field')
        if not re.match(empty_string_pattern,chats):
            messages.info(req,'Chat cannot be empty or just spaces!')
        else:
            chat_save = ChatMessages.objects.create(
                chat_prod_id = product,
                msg_from = buy_id,
                msg_to = sell_id,
                msg_type = 'coming',
                message = chats
            )
            chat_save.save()
            return HttpResponseRedirect(reverse('sellerchat', args=(prod_id, buy_id, sell_id)))
    chatmessages = ChatMessages.objects.filter(chat_prod_id=prod_id).filter(msg_from=buy_id).filter(msg_to=sell_id).values()
    return render(req,'sellerchat.html',context={
        'id':req.user.id,
        'chatmessages':chatmessages,
        'product':product,
        'buyer':buyer,
    })
    
    
@login_required(login_url='/login/')
def userprofile(req,id):
    user = CustomUser.objects.filter(id=id).first()
    if req.method == 'POST':
        first_name = req.POST.get('user-firstname')
        last_name = req.POST.get('user-lastname')
        email= req.POST.get('user-email')
        phone = req.POST.get('user-phone')
        username = req.POST.get('user-username')
        address = req.POST.get('user-address')
        CustomUser.objects.filter(id=id).update(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            username=username,
            address=address    
        )
        messages.success(req,'Profile Saved!')
        return HttpResponseRedirect(reverse('userprofile', args=(id,)))
    return render(req,'userprofile.html',context={
        'id':id,
        'user':user,
    })