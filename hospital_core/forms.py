from django import forms
from patients.models import Patient
from doctors.models import Doctor
from django import forms


class NotificationForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)


class PatientLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Email or Phone Number'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))


class DoctorLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
