
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']  

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
                return redirect('register')
            
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.info(request, "Registration successful!")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")  
            return redirect('register')

    return render(request, "registration.html")





def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('newpage')
        else:
            messages.info(request, "invalid register")
            return redirect('login')
    return render(request, 'log.html')

def newpage(request):
    return render(request, 'newpage.html')

def logout(request):
    auth.logout(request)
    return redirect('/')