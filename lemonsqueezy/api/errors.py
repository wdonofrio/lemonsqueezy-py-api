from functools import wraps
from typing import Any, Callable, Dict

import requests


class LemonSqueezyError(Exception):
    """Base class for LemonSqueezy API errors."""

    def __init__(
        self, message: str, status_code: int, response_json: Dict[str, Any]
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.response_json = response_json


class LemonSqueezyClientError(LemonSqueezyError):
    """Base class for LemonSqueezy API client errors. (4xx)"""


class LemonSqueezyServerError(LemonSqueezyError):
    """Base class for LemonSqueezy API server errors. (5xx)"""


def handle_http_errors(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except requests.exceptions.HTTPError as e:
            if 400 <= e.response.status_code < 500:
                raise LemonSqueezyClientError(
                    f"Client error: {e.response.status_code}. {e.response.json().get('errors')}",
                    status_code=e.response.status_code,
                    response_json=e.response.json(),
                ) from e
            elif 500 <= e.response.status_code < 600:
                raise LemonSqueezyServerError(
                    f"Server error: {e.response.status_code}. {e.response.json().get('errors')}",
                    status_code=e.response.status_code,
                    response_json=e.response.json(),
                ) from e
            else:
                raise LemonSqueezyError(
                    f"An error occurred. {e.response.json().get('errors')}",
                    status_code=e.response.status_code,
                    response_json=e.response.json(),
                ) from e

    return wrapper
