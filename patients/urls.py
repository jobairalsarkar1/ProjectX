from django.urls import path
from . import views

urlpatterns = [
    path('patients_dashboard/', views.patients_dashboard, name='patients_dashboard'),
    path('patients_account/', views.patients_account, name='patients_account'),
    path('patients_inbox/', views.patients_inbox, name='patients_inbox'),
    path('patients_settings/', views.patients_settings, name='patients_settings')
]