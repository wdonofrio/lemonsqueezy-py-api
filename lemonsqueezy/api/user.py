import requests

from lemonsqueezy.api import BASE_URL, get_headers
from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.user import User


@handle_http_errors
def get_user() -> User:
    """Get the user"""
    response = requests.get(f"{BASE_URL}/users/me", headers=get_headers(), timeout=30)
    response.raise_for_status()
    user_data = response.json().get("data", {})
    return User(**user_data)
