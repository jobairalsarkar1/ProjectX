from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='Home'),
    path('blog/', views.blog, name='Blog'),
    path('service/', views.service, name='Service'),
    path('about/', views.about, name='About'),
    path('register/', views.PatientRegister, name='Register'),
    path('patient_login/', views.patient_login_view, name='PatientLogin'),
    path('doctor_login/', views.doctor_login_view, name='DoctorLogin')
]