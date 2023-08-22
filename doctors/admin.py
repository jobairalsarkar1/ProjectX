from django.contrib import admin
from doctors.models import Doctor, Assignment, DoctorNotification

admin.site.register(Doctor)
admin.site.register(Assignment)
admin.site.register(DoctorNotification)