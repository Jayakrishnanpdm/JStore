from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
from . models import Customer,UserOpinion

# Create your views here.
def account(request):
    reg_error_message=None
    login_error_message=None
    sucess_message=None
    if request.POST:
        form=request.POST.get('form')
        if form=='reg_form' :
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            address=request.POST.get('address')
            try:
                user=User.objects.create_user(username=username,password=password,email=email)
                customer=Customer.objects.create(phone=phone,address=address,user=user)
                sucess_message='User created sucessfully'
            except Exception as e:
               reg_error_message = 'User already exists'  

        if form=='login_form' :
            username=request.POST.get('username')
            password=request.POST.get('password')   
            try:
                user=authenticate(username=username,password=password)
                authlogin(request,user)
                return redirect('home')
            except Exception as e:
                login_error_message='Incorrect User Credentials'              
    return render(request,'account.html',{'reg_error_message':reg_error_message,'login_error_message':login_error_message,'sucess_message':sucess_message})
    
def logout(request):
    authlogout(request)
    return redirect('account')

def contact_us(request):
    if request.POST:
        name=request.POST.get('Name')
        email=request.POST.get('Email')
        message=request.POST.get('Message')
        user_opinion=UserOpinion.objects.create(name=name,email=email,message=message)
        return redirect('home')
    