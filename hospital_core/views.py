from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from patients.forms import PatientRegistrationForm
from django.contrib import messages
from doctors.models import Doctor
from patients.models import Patient
<<<<<<< HEAD
from .models import Notification
=======
# from .models import Notification
>>>>>>> 5d3e795c5a006da4b1fb513aedfb09e605a2f3e3


def landing_view(request):
    return render(request, 'landing.html')


def blog(request):
    return render(request, 'blog.html')


def service(request):
    return render(request, 'service.html')


def about(request):
    return render(request, 'about.html')


def PatientRegister(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Patient.objects.filter(email=email).exists():
                messages.error(request, 'This Email is already Used.')
            else:
                password = form.cleaned_data['password']
                retype_password = form.cleaned_data['retype_password']

                if password == retype_password:
                    form.save()
                    return redirect('PatientLogin')
                else:
                    messages.error(request, 'Password did not matched.')
    else:
        form = PatientRegistrationForm()
    return render(request, 'register.html', {'form': form})


def doctor_login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            doctor = Doctor.objects.get(email=email)
        except Doctor.DoesNotExist:
            error_message = 'Doctor with this email does not exist'
            return render(request, 'doctor_login.html', {'error_message': error_message})

        if check_password(password, doctor.password):
            request.session['doctor_id'] = doctor.id
            return redirect('doctors_dashboard')
        else:
            error_message = 'Incorrect password'
            return render(request, 'doctor_login.html', {'error_message': error_message})

    return render(request, 'doctor_login.html')


def patient_login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            patient = Patient.objects.get(email=email)
        except Patient.DoesNotExist:
            error_message = 'Patient with this email does not exist'
            return render(request, 'patient_login.html', {'error_message': error_message})

        if check_password(password, patient.password):
            request.session['patient_id'] = patient.id
            return redirect('patients_dashboard')
        else:
            error_message = 'Incorrect password'
            return render(request, 'patient_login.html', {'error_message': error_message})

    return render(request, 'patient_login.html')


def no_access(request):
    return render(request, '404.html')


# def compose_notification(request, receiver_type, receiver_id):
#     if request.method == 'POST':
#         message = request.POST.get('message')
#         sender_id = request.session.get(
#             'patient_id') or request.session.get('doctor_id')

#         if sender_id:
#             sender_type = 'patient' if request.session.get(
#                 'patient_id') else 'doctor'
#             sent_by_patient = sender_type == 'patient'

#             if receiver_type == 'doctor':
#                 receiver_model = Doctor
#             else:
#                 receiver_model = Patient

#             # receiver = receiver_model.objects.get(id=receiver_id)
#             Notification.objects.create(
#                 sender_id=sender_id, receiver_id=receiver_id, sent_by_patient=sent_by_patient, message=message)
#             return redirect('Blog')
#     return render(request, 'compose_notification.html', {'receiver_type': receiver_type, 'receiver_id': receiver_id})
#     doctor_id = request.session.get('doctor_id')
#     if doctor_id:
#         try:
#             doctor = Doctor.objects.get(id=doctor_id)
#             notifications = Notification.objects.filter(
#                 receiver_id=doctor_id, sent_by_patient=True)
#             return render(request, 'd_inbox.html', {'doctor': doctor, 'notifications': notifications})
#         except Doctor.DoesNotExist:
#             pass
#     return redirect('DoctorLogin')


