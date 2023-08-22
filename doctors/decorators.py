from functools import wraps
from django.shortcuts import redirect
from .models import Doctor

def doctor_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not Doctor.objects.filter(user=request.user).exists():
            return redirect("DoctorLogin")  # Redirect unauthorized users
        return view_func(request, *args, **kwargs)
    return _wrapped_view
