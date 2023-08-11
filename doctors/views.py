from django.shortcuts import render

def doctor_dashboard(request):
    return render(request, 'd_dashboard.html')

def doctor_profile(request):
    return render(request, 'd_profile.html')

def doctor_inbox(request):
    return render(request, 'd_inbox.html')

def doctor_settings(request):
    return render(request, 'd_settings.html')