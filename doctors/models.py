from django.db import models
from hospital_core.models import Department, Room
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Doctor(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f"Doctor->{self.fname} {self.lname}"

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Assignment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.Case)
