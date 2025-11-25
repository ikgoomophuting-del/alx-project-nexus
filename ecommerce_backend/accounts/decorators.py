from django.http import HttpResponseForbidden
from functools import wraps

def role_required(allowed_roles):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Authentication required")
            if request.user.role not in allowed_roles:
                return HttpResponseForbidden("Insufficient role")
            return func(request, *args, **kwargs)
        return wrapper
    return decorator
