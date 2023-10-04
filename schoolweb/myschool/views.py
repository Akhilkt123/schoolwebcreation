from django.shortcuts import render, redirect
from .models import RegForm
from django.contrib import messages
from .forms import RegForm 

def home(request):
    return render(request,'home.html')



def regform(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
           

            messages.success(request, "Order confirmed. Registration successful.")
            return redirect('home') 
        else:
            messages.info(request, "Order confirmed. Registration successfully.")
    else:
        form = RegForm()

    return render(request, 'regform.html', {'form': form})

