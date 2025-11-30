from django.http import JsonResponse

class RoleRequiredMiddleware:
    """
    Optional middleware that checks if a request has a valid user role.
    You can expand this logic later if needed.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow request to proceed
        return self.get_response(request)
