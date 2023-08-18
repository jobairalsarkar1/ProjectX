from django.shortcuts import render, redirect
from django.http import HttpResponse
from patients.models import Patient
from doctors.models import Doctor
from django import forms
from django.contrib.auth.forms import UserCreationForm
from  hospital_core.forms import SignupForm
from django.contrib.auth import login

def landing_view(request):
    return render(request, 'landing.html')

def blog(request):
    return render(request, 'blog.html')

def service(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    if request.method == 'POST':
        form = SignupFrom(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})
    
    

#create login logout
#date time module for forgotten password
#dynamic email
#hashing 