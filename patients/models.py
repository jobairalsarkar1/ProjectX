from django.db import models
from doctors.models import Doctor
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=200)
    birth_date = models.DateField(default=timezone.now)
    profile_picture = models.ImageField(
        upload_to='patients_profile_picture', default='patient.jpg')

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

    def __str__(self) -> str:
        return f"Patient->{self.first_name} {self.last_name}"


class MedicalRecord(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    conditions = models.TextField()


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField(unique=True)

    def __str__(self) -> str:
        return f"Appointment NO -> {self.id}"

    class Meta:
        unique_together = ('doctor', 'date')

