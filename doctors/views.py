from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import Doctor
from patients.models import Patient, Appointment
from hospital_core.models import Department
from .decorators import doctor_required
from django.contrib.auth import logout

# @doctor_required
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

# @doctor_requåired
def doctor_profile(request):
    doctor_id = request.session.get('doctor_id')
    if doctor_id:
        try:
            doctor = Doctor.objects.get(id=doctor_id)
            appointments_done = Appointment.objects.filter(doctor=doctor)
            appointments = Appointment.objects.filter(doctor=doctor)
            unique_patients = Patient.objects.filter(appointment__in=appointments).distinct()
            unique_patients_number = unique_patients.count()
            return render(request, 'd_profile.html', {'doctor':doctor, 'unique_patients_number':unique_patients_number, 'appointments_done':appointments_done})
        except Doctor.DoesNotExist:
            pass
    return redirect('DoctorLogin')

# @doctor_required
def doctor_inbox(request):
    doctor_id = request.session.get('doctor_id')
    if doctor_id:
        try:
            doctor = Doctor.objects.get(id=doctor_id)
            return render(request, 'd_inbox.html', {'doctor':doctor})
        except Doctor.DoesNotExist:
            pass
    
    return redirect('DoctorLogin')

def doctor_settings(request):
    doctor_id = request.session.get('doctor_id')
    if doctor_id:
        try:
            doctor = Doctor.objects.get(id=doctor_id)
            return render(request, 'd_settings.html', {'doctor':doctor})
        except Doctor.DoesNotExist:
            pass
    return redirect('DoctorLogin')

# def authenticate_doctor(email, password):
#     try:
#         doctor = Doctor.objects.get(email=email)
#         if doctor.password == password:
#             return doctor
#         else:
#             return 'Invalid Password'
#     except Doctor.DoesNotExist:
#         return 'No Doctor with this Email.'

def doctor_logout(request):
    logout(request)
    return redirect('DoctorLogin')
