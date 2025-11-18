import time
import logging

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    """
    Logs the request method, path, and how long the request took.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = time.time()

        response = self.get_response(request)

        duration = time.time() - start_time
        method = request.method
        path = request.get_full_path()

        logger.info(
            f"[REQUEST] {method} {path} completed in {duration:.2f} seconds"
        )

        return response
