from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User

from django.contrib import messages

def authlogin(request):

    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request,username=name, password=password)

        if user is not None:
            login(request, user)
            return redirect('employee.profile')
        else:
            messages.error(request, 'Email or password invalid!')


    return render(request,'authentication/login.html')

def authregistration(request):
    if request.method == 'POST':
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_Password=request.POST['confirm_Password']

        if password==confirm_Password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif  User.objects.filter(email=email).exists():
                messages.error(request, 'email already exists')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')


        else:
            messages.error(request, 'Password & Comfirm_password not match!')


    return render(request,'authentication/registration.html')

def forgotpassword(request):
    return render(request,'authentication/forgot.html')
def userlogout(request):
    logout(request)
    messages.success(request, 'Successfuly Logout!')
    return redirect('login')


