from django.shortcuts import render
from django.http import HttpResponse


def landing_view(request):
    return render(request, 'landing.html')


def blog(request):
    return render(request, 'blog.html')


def service(request):
    return render(request, 'service.html')


def about(request):
    return render(request, 'about.html')


def PatientRegister(request):
    return render(request, 'base.html')
