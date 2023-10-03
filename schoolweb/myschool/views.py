from django.shortcuts import render, redirect
from .models import RegForm
from django.contrib import messages

def home(request):
    return render(request,'home.html')



def regform(request):
    if request.method == 'POST':
      
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('regsuccess') 
            messages.success(redirect,"order confirm")
            return redirect('regsuccess')
    else:
       
        form = RegForm()

    return render(request, 'regform.html', {'form': form})

def reg_success(request):
    return render(request, 'regsuccess.html')  

