from django.urls import path
from . import views

urlpatterns = [
    path('doctors_dashboard/', views.doctor_dashboard, name='doctors_dashboard'),
    path('doctors_profile/', views.doctor_profile, name='doctors_profile'),
    path('doctors_inbox/', views.doctor_inbox, name='doctors_inbox'),
    path('doctors_settings/', views.doctor_settings, name='doctors_settings'),
    path('doctor_logout/', views.doctor_logout, name='doctor_logout'),
    path('patients_list/', views.doctor_patients_list, name='doctor_patients_list'),
    path('send_notifiction/<int:patient_id>', views.send_notification, name='send_notification'),
    path('update-doctor-profile/', views.update_doctor_profile, name='update_doctor_profile'),
]