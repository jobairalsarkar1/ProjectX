from . import views
from django.urls import path

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('admin_login/', views.admin_login, name = 'admin_login'),

    #This Section Handles Doctors
    path('doctors/', views.DoctorView.as_view(), name = 'doctors'),
    path('doctors/add/', views.doctor_creation_view, name = 'add_doctor'),
    path('doctors/update/<int:id>', views.doctor_update, name = 'update_doctor'),
    path('doctors/delete/<int:id>', views.doctor_delete_view, name="delete_doctor"),
    path('doctors/search/', views.search_doctor, name="search_doctor"),
    path('doctors/filter/', views.filter_doctor, name="filter_doctor"),

    #This Section Handles Patient
    path('patients/', views.PatientView.as_view(), name = 'patients'),
    path('patients/add', views.patient_creation_view, name = 'add_patient'),
    path('patients/update/<int:id>', views.patient_update, name = 'update_patient'),
    path('patients/delete/<int:id>', views.patient_delete_view, name="delete_patient"),
    path('patients/search/', views.search_patient, name="search_patient"),
]