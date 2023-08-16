from django.db import models
from doctors.models import Doctor
from django.utils import timezone

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    password = models.CharField(max_length=200)
    birth_date = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return f"Patient->{self.first_name} {self.last_name}"


class MedicalRecord(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    conditions = models.TextField()

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()