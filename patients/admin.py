from django.contrib import admin
from patients.models import Patient, Appointment, MedicalRecord

admin.site.register(Patient)
admin.site.register(MedicalRecord)
admin.site.register(Appointment)