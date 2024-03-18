from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from userAuthenticate.models import CustomUser
from products.models import Products
from django.contrib import messages

# Create your views here.
def login_user(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        password = req.POST.get('password')
        
        if not CustomUser.objects.filter(email=email).exists():
            messages.error(req,'User does not exists.')
            return redirect('login')
        elif email=='admin@gmail.com' and password=='Drc@1234':
            user = authenticate(req,email=email,password=password)
            if user is None:
                messages.error(req,'Wrong password')
            else:
                login(req,user)
                return redirect('/adminpanel')
        else:
            user = authenticate(req,email=email,password=password)
            if user is None:
                messages.error(req,'Wrong password')
            else:
                login(req,user)
                return redirect(f'/user/{user.id}') 
    return render(req,'login.html')



def signup(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        email = req.POST.get('email')
        firstname = req.POST.get('firstname')
        lastname = req.POST.get('lastname')
        phone = req.POST.get('phone')
        address = req.POST.get('address')
        password = req.POST.get('password')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.info(req,'Email already exists!')
            return redirect('signup')
        else:
            user = CustomUser.objects.create_user(
                username = username,
                email=email,
                first_name = firstname,
                last_name = lastname,
                phone = phone,
                address = address,
                password = password
            )
            user.save()
            user = authenticate(req,email=email,password=password)
            login(req,user)
            return redirect(f'/user/{user.id}')
    return render(req,'signup.html')



@login_required(login_url='/login/')
def logout_user(req):
    logout(req)
    return redirect('home')


@login_required(login_url='/login/')
def adminpage(req):
    print(req)
    return render(req,'adminpanel.html')


@login_required(login_url='/login/')
def userhome(req,id):
    products = Products.objects.all()
    return render(req,'homepage.html',context={
        'products':products,
        'id':id,
    })