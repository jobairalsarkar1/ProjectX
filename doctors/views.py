from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import Doctor, DoctorNotification
from patients.models import Patient, Appointment
from hospital_core.models import Department
from .decorators import doctor_required
from django.contrib.auth import logout
from hospital_core.forms import DoctorUpdateForm

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
            unique_patients = Patient.objects.filter(
                appointment__in=appointments).distinct()
            unique_patients_number = unique_patients.count()
            return render(request, 'd_profile.html', {'doctor': doctor, 'unique_patients_number': unique_patients_number, 'appointments_done': appointments_done})
        except Doctor.DoesNotExist:
            pass
    return redirect('DoctorLogin')


def update_doctor_profile(request):
    doctor_id = request.session.get('doctor_id')
    doctor = request.session.get('doctor_id')
    if doctor_id:
        try:
            doctor = Doctor.objects.get(id=doctor_id)
            if request.method == 'POST':
                form = DoctorUpdateForm(
                    request.POST, request.FILES, instance=doctor)
                if form.is_valid():
                    form.save()
                    return redirect('doctors_profile')
            else:
                form = DoctorUpdateForm(instance=doctor)
            return render(request, 'd_settings.html', {'form': form, 'doctor': doctor})
        except Doctor.DoesNotExist:
            pass

    return redirect('DoctorLogin')


def doctor_inbox(request):
    doctor_id = request.session.get('doctor_id')
    if doctor_id:
        try:
            doctor = Doctor.objects.get(id=doctor_id)
            return render(request, 'd_inbox.html', {'doctor': doctor})
        except Doctor.DoesNotExist:
            pass

    return redirect('DoctorLogin')


def doctor_settings(request):
    doctor_id = request.session.get('doctor_id')
    if doctor_id:
        try:
            doctor = Doctor.objects.get(id=doctor_id)
            return render(request, 'd_settings.html', {'doctor': doctor})
        except Doctor.DoesNotExist:
            pass
    return redirect('DoctorLogin')


def doctor_logout(request):
    logout(request)
    return redirect('DoctorLogin')


def doctor_patients_list(request):
    doctor_id = request.session.get('doctor_id')
    if doctor_id:
        try:
            doctor = Doctor.objects.get(id=doctor_id)
            patients = Patient.objects.filter(
                appointment__doctor=doctor).distinct()
            return render(request, 'doctor_patients_list.html', {'doctor': doctor, 'patients': patients})
        except Doctor.DoesNotExist:
            pass
    return redirect('DoctorLogin')


def send_notification(request, patient_id):
    doctor_id = request.session.get('doctor_id')
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        sender = Doctor.objects.get(id=request.session['doctor_id'])
        recipient = Patient.objects.get(id=patient_id)

        attachment = None
        if request.FILES.get('attachment'):
            attachment = request.FILES['attachment']

        notification = DoctorNotification(
            sender=sender, recipient=recipient, subject=subject, message=message, attachment=attachment)
        notification.save()
        return redirect('doctor_patients_list')
    else:
        try:
            patient = Patient.objects.get(id=patient_id)
            doctor = Doctor.objects.get(id=doctor_id)
            return render(request, 'send_notification.html', {'patient': patient, 'doctor': doctor})
        except Patient.DoesNotExist:
            pass
    return redirect('DoctorLogin')
