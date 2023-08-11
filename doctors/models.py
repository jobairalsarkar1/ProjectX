from django.db import models
from hospital_core.models import Department, Room

class Doctor(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=300)

class Assignment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.Case)