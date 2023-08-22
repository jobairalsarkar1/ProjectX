from django.shortcuts import redirect
from .models import Doctor

class RestrictDoctorAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is a doctor and trying to access patient-related views
        if request.user.is_authenticated and isinstance(request.user, Doctor) and "patient" in request.path:
            return redirect("doctors_dashboard")  # Redirect doctors to their dashboard

        response = self.get_response(request)
        return response
