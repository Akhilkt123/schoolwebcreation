from Tools.scripts.make_ctype import method
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import message
from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password,)

                user.save();
                return redirect('login')

        else:
            messages.info(request, "password not matching") 
            return redirect('register')
        return redirect('/')
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
            messages.error(request, "Invalid login credentials")
            return redirect('login')  
    else:
        return render(request, 'log.html') 

    
    return HttpResponse("Invalid request") 

def newpage(request):
    return render(request, 'newpage.html')

def logout(request):
    auth.logout(request)
    return redirect('/')