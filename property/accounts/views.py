from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from contacts.models import Contact
from django.http import JsonResponse
from django.http import HttpResponse


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:

            auth.login(request,user)
            messages.success(request,'Successfully logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')

    else:    
        return render(request,'accounts/login.html')


def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'You are logged out')
        return redirect('index')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        #password check
        if password==password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'That Username is taken')
                return redirect('register') 
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'That Email already exist')
                    return redirect('register')
                else:
                    user=User(username=username,email=email,first_name=first_name,last_name=last_name,password=password)
                    user.set_password(password)
                    user.save()
                    messages.success(request,'You are successfully registred')
                    return redirect('login')
        else:
            messages.error(request,'Password so not match')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')




def dashboard(request):
    user_contacts=Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context={
        'contacts':user_contacts
    }
    print(context)
    return render(request,'accounts/dashboard.html',context)