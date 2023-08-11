from django.db import models
from doctors.models import Doctor

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    password = models.CharField(max_length=200)
    birth_date = models.DateField()


class MedicalRecord(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    conditions = models.TextField()

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()