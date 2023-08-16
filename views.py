from django.shortcuts import render
from django.http import HttpResponse
from patients.models import Patient
from doctors.models import Doctor
from django import forms
from django.contrib.auth.forms import UserCreationForm
from hospital_core.forms import SignupForm
from render_block import render_block_to_string 

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
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'form': SignupForm()}
        else:
            context = {'form': form}
        html1 = render_block_to_string('base.html', 'sign-up-form', context)
        return HttpResponse(html1)
    context = { 'form': SignupForm(),
               'patients': Patient.objects.all()}
    
    