from typing import Protocol


class LemonSqueezyProtocol(Protocol):
    """Protocol defining the required interface for a LemonSqueezy client"""

    @property
    def headers(self) -> dict[str, str]:
        """Return the headers for the request"""
        raise NotImplementedError

    @property
    def base_url(self) -> str:
        """Return the base URL for the API"""
        raise NotImplementedError
