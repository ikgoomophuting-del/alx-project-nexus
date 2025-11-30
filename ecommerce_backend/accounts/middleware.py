from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden

class RoleRequiredMiddleware(MiddlewareMixin):
    """
    Example placeholder — customize as needed.
    """
    def process_request(self, request):
        # example: skip for anonymous / static etc
        return None
