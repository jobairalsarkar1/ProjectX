from django import forms
from .models import Patient
from django.core.validators import validate_email


class PatientRegistrationForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email or Phone Number'}),
        validators=[validate_email],)
    retype_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Re-type Password'}))

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            # 'email': forms.TextInput(attrs={'placeholder': 'Email or Phone Number'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }
