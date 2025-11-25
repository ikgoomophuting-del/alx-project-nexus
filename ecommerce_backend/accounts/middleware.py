from django.shortcuts import redirect

class RoleBasedRedirectMiddleware:
    """
    Example middleware — adapt the mapping as needed.
    If a user tries to access an admin-only path and isn't admin, redirect to home.
    """
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        # only apply for authenticated users
        path = request.path
        if path.startswith("/admin/") and request.user.is_authenticated and not request.user.is_staff:
            return redirect("/")
        return self.get_response(request)

