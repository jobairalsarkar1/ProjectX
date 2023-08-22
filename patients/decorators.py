from functools import wraps
from django.shortcuts import redirect
from .models import Patient

def patient_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not isinstance(request.user, Patient):
            return redirect("patients_dashboard")  # Redirect unauthorized users
        return view_func(request, *args, **kwargs)
    return _wrapped_view
