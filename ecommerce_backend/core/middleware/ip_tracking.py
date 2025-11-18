import logging

logger = logging.getLogger(__name__)

class IPTrackingMiddleware:
    """
    Logs the IP address of the user making the request.
    Useful for debugging, abuse detection, and analytics.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        ip = request.META.get('REMOTE_ADDR', 'Unknown IP')
        path = request.get_full_path()
        method = request.method

        logger.info(f"[IP] {ip} accessed {method} {path}")

        return self.get_response(request)
