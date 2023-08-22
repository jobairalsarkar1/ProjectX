from django import forms
from .models import Patient, Appointment
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils import timezone


class PatientRegistrationForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email or Phone Number'}),
        validators=[validate_email],)
    retype_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Re-type Password'}))

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            # 'email': forms.TextInput(attrs={'placeholder': 'Email or Phone Number'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }


class PatientUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name',
                  'phone', 'birth_date', 'profile_picture']


class AppointMentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time']

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if date and time:
            datetime_combined = datetime.combine(date, time)

            local_time = timezone.now().replace(tzinfo=None)
            if datetime_combined <= local_time:
                self.add_error(
                    'date', 'As it is not possible to go back in time choose date from the future.')
            existing_appointment = Appointment.objects.filter(
                date=datetime_combined).first()
            if existing_appointment:
                self.add_error('date', 'This Date & Time is already Reserved.')

            # Checks if time is between 9 AM to 4 PM
            if time.hour < 9 or time.hour >= 16:
                self.add_error(
                    'time', 'Appointments are only allowed between 9 AM and 4 PM.')

        return cleaned_data


# class NotificationForm(forms.ModelForm):
#     class Meta:
#         model = Notification
#         fields = ['subject', 'message', 'file']
