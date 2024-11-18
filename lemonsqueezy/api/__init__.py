from typing import Dict

from lemonsqueezy.config import settings

BASE_URL = settings.api_url


def get_headers() -> Dict[str, str]:
    """Get the headers for the request"""
    return {
        "Accept": "application/vnd.api+json",
        "Content-Type": "application/vnd.api+json",
        "Authorization": f"Bearer {settings.api_key}",
    }


__all__ = ["BASE_URL", "get_headers"]
