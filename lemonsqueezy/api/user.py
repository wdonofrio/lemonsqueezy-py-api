import requests

from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.user import User
from lemonsqueezy.protocols import LemonSqueezyProtocol


@handle_http_errors
def get_user(client: LemonSqueezyProtocol) -> User:
    """Get the user"""
    response = requests.get(
        f"{client.base_url}/users/me", headers=client.headers, timeout=30
    )
    response.raise_for_status()
    user_data = response.json().get("data", {})
    return User(**user_data)
