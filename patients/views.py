from django.shortcuts import render, redirect
from django.contrib.auth import logout
# from django.contrib.auth.hashers import check_password
# from django.contrib.auth.decorators import login_required
# from .decorators import patient_required
from .models import Patient, Appointment
from doctors.models import Doctor, DoctorNotification
from .forms import AppointMentForm, PatientUpdateForm
from datetime import datetime


# @patient_required
def patients_dashboard(request):
    patient_id = request.session.get('patient_id')
    if patient_id:
        try:
            patient = Patient.objects.get(id=patient_id)
            appointments = Appointment.objects.filter(patient=patient)
            return render(request, 'p_dashboard.html', {'patient': patient, 'appointments': appointments})
        except Patient.DoesNotExist:
            pass

    return redirect('PatientLogin')


# @patient_required
def patients_account(request):
    patient_id = request.session.get('patient_id')
    if patient_id:
        try:
            patient = Patient.objects.get(id=patient_id)
            appointments = Appointment.objects.filter(patient=patient)
            total_appointments = get_patients_total_appointment(patient_id)
            return render(request, 'p_account.html', {'patient': patient, 'appointments': appointments, 'total_appointments': total_appointments})
        except Patient.DoesNotExist:
            pass

    return redirect('PatientLogin')


# @patient_required
def patients_inbox(request):
    patient_id = request.session.get('patient_id')
    if patient_id:
        try:
            patient = Patient.objects.get(id=patient_id)
            notifications = DoctorNotification.objects.filter(recipient = patient).order_by('-timestamp')
            return render(request, 'p_inbox.html', {'patient': patient, 'notifications':notifications})
        except Patient.DoesNotExist:
            pass

    return redirect('PatientLogin')

def update_patient_profile(request):
    patient_id = request.session.get('patient_id')
    patient = Patient.objects.get(id=patient_id)
    if patient_id:
        try:
            patient = Patient.objects.get(id=patient_id)
            if request.method == 'POST':
                form = PatientUpdateForm(request.POST, request.FILES, instance=patient)
                if form.is_valid():
                    form.save()
                    return redirect('patients_account')
            else:
                form = PatientUpdateForm()
            return render(request, 'p_settings.html', {'form':form, 'patient':patient})
        except Patient.DoesNotExist:
            pass
    return redirect('PatientLogin')


def patients_settings(request):
    patient_id = request.session.get('patient_id')
    if patient_id:
        try:
            patient = Patient.objects.get(id=patient_id)
            appointments = Appointment.objects.filter(patient=patient)
            return render(request, 'p_settings.html', {'patient': patient, 'appointments': appointments})
        except Patient.DoesNotExist:
            pass

    return redirect('PatientLogin')


# def authenticate_patient(email, password):
#     try:
#         patient = Patient.objects.get(email=email)
#         if patient.password == password:
#             return patient
#         else:
#             return 'Invalid Password!'
#     except Patient.DoesNotExist:
#         return 'No Patient with this Email'

def patient_logout(request):
    logout(request)
    return redirect('PatientLogin')


def doctor_list(request):
    patient_id = request.session.get('patient_id')
    if patient_id:
        try:
            patient = Patient.objects.get(id=patient_id)
            doctors = Doctor.objects.all()
            appointments = Appointment.objects.all()
            return render(request, 'doctor_list.html', {'doctors': doctors, 'appointments': appointments, 'patient': patient})
        except Patient.DoesNotExist:
            pass
    return redirect('PatientLogin')


def reserve_appointment(request, doctor_id):
    patient_id = request.session.get('patient_id')
    patient = Patient.objects.get(id=patient_id)
    if not patient_id:
        return redirect('PatientLogin')

    doctor = Doctor.objects.get(id=doctor_id)

    if request.method == 'POST':
        form = AppointMentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            datetime_combined = datetime.combine(appointment.date, form.cleaned_data['time'])
            appointment.date = datetime_combined
            try:
                patient = Patient.objects.get(id=patient_id)
                appointment.patient = patient
                appointment.save()
                return redirect('doctor_list')
            except Patient.DoesNotExist:
                pass
    else:
        form = AppointMentForm()
    return render(request, 'reserve_appointment.html', {'doctor': doctor, 'form': form, 'patient': patient})


def cancel_appointment(request, appointment_id):
    patient_id = request.session.get('patient_id')
    if not patient_id:
        return redirect('PatientLogin')

    try:
        appointment = Appointment.objects.get(
            id=appointment_id, patient_id=patient_id)
        appointment.delete()
    except Appointment.DoesNotExist:
        pass

    return redirect('patients_account')


# Necessary Third party function.
def get_patients_total_appointment(patient_id):
    try:
        patient = Patient.objects.get(id=patient_id)
        total_appointments = patient.appointment_set.count()
        return total_appointments
    except Patient.DoesNotExist:
        return 0
