from django.db import models
from hospital_core.models import Department, Room
from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from io import BytesIO


class Doctor(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=300)
    profile_picture = models.ImageField(
        upload_to='doctors_profile_picture', default='doctor.jpg')
    fees = models.DecimalField(max_digits=6, decimal_places=2, default=500)

    def __str__(self) -> str:
        return f"Doctor -> {self.fname} {self.lname}"

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

        if self.profile_picture:
            img = Image.open(self.profile_picture.path)
            bytes_memory = BytesIO()

            if img.format == 'JPEG':
                format_extention = 'JPEG'
                quality = 20
            elif img.format == 'PNG':
                format_extention = 'PNG'
                quality = None
            else:
                format_extention = 'JPEG'
                quality = 20

            img.save(bytes_memory, format=format_extention, quality=quality)
            self.profile_picture = InMemoryUploadedFile(
                bytes_memory, 'ImageField', self.profile_picture.name, f'image/{format_extention.lower()}', bytes_memory.tell(), None)
            super().save(*args, **kwargs)


class Assignment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.Case)
