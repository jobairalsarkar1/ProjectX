<<<<<<< HEAD
from django.shortcuts import render, redirect
from doctors.models import Doctor
from patients.models import Patient, Appointment
from hospital_core.models import Department
from django.views import View
from .forms import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required(login_url='/adminsite/admin_login')
def admin_dashboard(request):
    return render(request, 'base/dashboard.html')


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        print(user)
        if user:
            login(request, user)
            return redirect('admin_dashboard')
    return render(request, 'base/login.html')

################################################### Create and Read Views Goes Here ########################################
class DoctorView(View):
    def get(self, request):
        doctors = Doctor.objects.all()
        return render(request, 'doctors/doctors.html', {'doctors': doctors})

    def post(self, request):
        form = DoctorCreationForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            if Doctor.objects.filter(email = data.email):
                messages.warning(request, "Doctor with this Mail Already Exits")
                return redirect('add_doctor')
            else:
                data.save()
        return redirect('doctors')


class PatientView(View):
    def get(self, request):
        patients = Patient.objects.all()
        return render(request, 'patients/patients.html', {'patients': patients})

    def post(self, request):
        form = PatientCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('patients')

class DepartmentView(View):
    def get(self, request):
        departments = Department.objects.all()
        return render(request, 'departments/departments.html', {'departments':departments})

    def post(self, request):
        form = DepartmentCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('departments')
        
        return redirect('add_department')


class AppointmentView(View):
    def get(self, request):
        appointments = Appointment.objects.all()
        return render(request, 'appointments/appointments.html', {'appointments':appointments})

    def post(self, request):
        pass

#################################################   Update views goes Here  ################################################

def doctor_update(request, id):
    doctor = Doctor.objects.get(id=id)
    form = DoctorCreationForm(instance=doctor)
    if request.method == "POST":
        form = DoctorCreationForm(request.POST, request.FILES,  instance=doctor)
        print(form)
        form.save()
        return redirect('doctors')
    return render(request, 'doctors/update_doctor.html', {'form': form})


def patient_update(request, id):
    patient = Patient.objects.get(id=id)
    form = PatientCreationForm(instance=patient)
    if request.method == "POST":
        form = PatientCreationForm(request.POST, instance=patient)
        form.save()
        return redirect('patients')
    return render(request, 'patients/update_patient.html', {'form': form})


###############################################  Delete view goes here    ###################################################

def patient_delete_view(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('patients')


def doctor_delete_view(request, id):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('doctors')


def department_delete_view(request, id):
    department = Department.objects.get(id=id)
    department.delete()
    return redirect('departments')

def appointment_delete_view(request, id):
    appointment = Appointment.objects.get(id=id)
    appointment.delete()
    return redirect('appointments')


# Helpers View Goes Here
def doctor_creation_view(request):
    return render(request, 'doctors/create_doctor.html', {'form': DoctorCreationForm()})


def patient_creation_view(request):
    return render(request, 'patients/create_patient.html', {'form': PatientCreationForm()})


def department_creation_view(request):
    return render(request, 'departments/create_department.html', {'form': DepartmentCreationForm()})



# Search

def search_doctor(request):
    if request.method == 'POST':
        value = request.POST.get('value')
        if not value:
            return redirect('doctors')
        searched_doctor = Doctor.objects.filter(Q(fname__icontains=value) | 
        Q(email__icontains=value) | Q(lname__icontains=value))

    return render(request, 'doctors/doctors.html', {'doctors': searched_doctor})


def search_patient(request):
    if request.method == 'POST':
        value = request.POST.get('value')
        if not value:
            return redirect('patients')
        searched_patients = Patient.objects.filter(
            Q(first_name__icontains=value) | Q(last_name__icontains=value) | Q(phone__icontains=value) |
            Q(email__icontains=value)
        )

    return render(request, 'patients/patients.html', {'patients': searched_patients})

def search_appointment(request):
    if request.method == 'POST':
        value = request.POST.get('value')
        if not value:
            return redirect('appointments')
        appointments = Appointment.objects.filter(Q(patient__first_name__icontains = value) | Q(patient__last_name__icontains = value) )
    return render(request, 'appointments/appointments.html', {'appointments':appointments})
#filter

def filter_doctor(request):
    if request.method == 'POST':
        option = request.POST.get("options")
        doctors = Doctor.objects.filter(department__name__iexact = option)
        print(doctors)
    return render(request, 'doctors/doctors.html', {'doctors': doctors})
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> parent of 35520cb (Merge pull request #3 from undefined2001/test)
