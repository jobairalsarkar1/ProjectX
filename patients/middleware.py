from django.shortcuts import redirect
from .models import Patient

class RestrictPatientAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is a patient and trying to access doctor-related views
        if request.user.is_authenticated and isinstance(request.user, Patient) and "doctor" in request.path:
            return redirect("patients_dashboard")  # Redirect patients to their dashboard

        response = self.get_response(request)
        return response
