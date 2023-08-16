from django import forms
from django.contrib.auth.forms import UserCreationForm
from patients.models import Patient


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    
    class Meta:
        model = Patient 
        fields = ('first_name', 'last_name', 'email', 'phone', 'password', 'birth_date')