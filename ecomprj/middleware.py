import logging

logger = logging.getLogger(__name__)


class RequestResponseLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Логування перед обробкою запиту
        logger.info(f"Request: {request.method} {request.get_full_path()}")

        response = self.get_response(request)
        if (
            hasattr(response, "context_data")
            and "form" in response.context_data
            and hasattr(response.context_data["form"], "errors")
            and "__all__" in response.context_data["form"].errors
            and response.context_data["form"].errors["__all__"]
        ):
            errors = response.context_data["form"].errors["__all__"].data
            for err in errors:
                # Логування після обробки запиту
                is_message = hasattr(err, "message")
                message = err.message if is_message else "some error"
                logger.info(f"Response: {err.code} {message}")

        return response
