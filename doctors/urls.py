from django.urls import path
from . import views

urlpatterns = [
    path('doctors_dashboard/', views.doctor_dashboard, name='doctors_dashboard'),
    path('doctors_profile/', views.doctor_profile, name='doctors_profile'),
    path('doctors_inbox/', views.doctor_inbox, name='doctors_inbox'),
    path('doctors_settings/', views.doctor_settings, name='doctors_settings')
]