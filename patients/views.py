from django.shortcuts import render, redirect
from .models import Patient
from django.contrib.auth.hashers import check_password


def patients_dashboard(request):
    patient_id = request.session.get('patient_id')
    if patient_id:
        try:
            patient = Patient.objects.get(id=patient_id)
            return render(request, 'p_dashboard.html', {'patient': patient})
        except Patient.DoesNotExist:
            pass

    return redirect('PatientLogin')
    # return render(request, 'p_dashboard.html')


def patients_account(request):
    return render(request, 'p_account.html')


def patients_inbox(request):
    return render(request, 'p_inbox.html')


def patients_settings(request):
    return render(request, 'p_settings.html')


# def authenticate_patient(email, password):
#     try:
#         patient = Patient.objects.get(email=email)
#         if patient.password == password:
#             return patient
#         else:
#             return 'Invalid Password!'
#     except Patient.DoesNotExist:
#         return 'No Patient with this Email'