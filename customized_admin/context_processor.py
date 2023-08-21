from patients.models import Patient
from doctors.models import Doctor

def get_all_users(request):
    total_patients = len(Patient.objects.all())
    total_doctors = len(Doctor.objects.all())
    total_users = total_patients + total_doctors
    return {'total_users':total_users, 'total_doctors':total_doctors}
