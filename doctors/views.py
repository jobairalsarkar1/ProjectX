from django.shortcuts import render, redirect
from .models import Doctor
from django.contrib.auth.hashers import check_password


def doctor_dashboard(request):
    doctor_id = request.session.get('doctor_id')
    if doctor_id:
        try:
            doctor = Doctor.objects.get(id=doctor_id)
            return render(request, 'd_dashboard.html', {'doctor': doctor})
        except Doctor.DoesNotExist:
            pass

    return redirect('DoctorLogin')
    # return render(request, 'd_dashboard.html')


def doctor_profile(request):
    return render(request, 'd_profile.html')


def doctor_inbox(request):
    return render(request, 'd_inbox.html')


def doctor_settings(request):
    return render(request, 'd_settings.html')


def authenticate_doctor(email, password):
    try:
        doctor = Doctor.objects.get(email=email)
        if doctor.password == password:
            return doctor
        else:
            return 'Invalid Password'
    except Doctor.DoesNotExist:
        return 'No Doctor with this Email.'
