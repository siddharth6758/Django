from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from products.models import Products
from django.contrib import messages

# Create your views here.
def home(req):
    return render(req,'base.html')

@login_required    
def delete_prod(req,prod_id):
    user = Products.objects.filter(prod_id=prod_id).values().first()
    if user['posted_by_id'] == req.user.id:
        Products.objects.filter(prod_id=prod_id).delete()
        messages.success(req,'Product has been deleted successfully!')
        return redirect(f'/user/{req.user.id}')
    else:
        messages.error(req,'Could not delete product!')
        return redirect(f'/user/{req.user.id}')


@login_required(login_url='/login/')
def rent_prod(req,prod_id):
    buyuserid = req.user.id
    selluserid = Products.objects.filter(prod_id=prod_id).values().first()
    selluserid = selluserid['posted_by_id']
    if buyuserid == selluserid:
        messages.info(req,'You cannot rent your own product!')
        return redirect(f'/user/{req.user.id}')
    return redirect(f'/rentprod/{prod_id}b{buyuserid}s{selluserid}')

@login_required(login_url='/login/')
def complete_order(req,prod_id,buy_id,sell_id):
    print(prod_id,buy_id,sell_id)
    return render(req,'rentpage.html',context={
        'id':buy_id,
    })