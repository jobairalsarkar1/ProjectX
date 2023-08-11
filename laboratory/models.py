from django.db import models
from doctors.models import Doctor
from patients.models import Patient

class LabTest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class LabResult(models.Model):
    test = models.ForeignKey(LabTest, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    result = models.TextField()
    date = models.DateTimeField()
