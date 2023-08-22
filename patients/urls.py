from django.urls import path
from . import views

urlpatterns = [
    path('patients_dashboard/', views.patients_dashboard, name='patients_dashboard'),
    path('patients_account/', views.patients_account, name='patients_account'),
    path('patients_inbox/', views.patients_inbox, name='patients_inbox'),
    path('patients_settings/', views.patients_settings, name='patients_settings'),
    path('patient_logout/', views.patient_logout, name='patient_logout'),
    path('update-patients-profile/', views.update_patient_profile, name='update_patient_profile'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('reserve/<int:doctor_id>/', views.reserve_appointment, name='reserve_appointment'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),

]