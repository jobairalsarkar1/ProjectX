from django import forms
from doctors.models import Doctor
from patients.models import Patient



#This Form Handles Doctor Creation and Update
class DoctorCreationForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'lname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control', 'type':'password'}),
            'department':forms.Select(attrs={'class':'form-control'}),
            'specialty':forms.TextInput(attrs={'class':'form-control'}),
        }



#This Form Handles Patient Creation and Update

class PatientCreationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control', 'type':'password'}),
            'birth_date':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
        }

##filtering form 

