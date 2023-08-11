from django.shortcuts import render


def patients_dashboard(request):
    return render(request, 'p_dashboard.html')


def patients_account(request):
    return render(request, 'p_account.html')


def patients_inbox(request):
    return render(request, 'p_inbox.html')


def patients_settings(request):
    return render(request, 'p_settings.html')
