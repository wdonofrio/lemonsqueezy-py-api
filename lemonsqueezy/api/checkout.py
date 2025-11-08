import requests

from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.checkout import Checkout
from lemonsqueezy.protocols import LemonSqueezyProtocol


@handle_http_errors
def get_checkout(client: LemonSqueezyProtocol, checkout_id: str) -> Checkout:
    """Fetch a single checkout by identifier."""
    response = requests.get(
        f"{client.base_url}/checkouts/{checkout_id}",
        headers=client.headers,
        timeout=30,
    )
    response.raise_for_status()
    checkout_data = response.json().get("data", {})
    return Checkout(**checkout_data)


@handle_http_errors
def list_checkouts(
    client: LemonSqueezyProtocol, page: int = 1, per_page: int = 10
) -> list[Checkout]:
    """List checkouts with pagination support."""
    checkouts: list[Checkout] = []
    while True:
        response = requests.get(
            f"{client.base_url}/checkouts?page[number]={page}&page[size]={per_page}",
            headers=client.headers,
            timeout=30,
        )
        response.raise_for_status()
        response_data = response.json()

        for checkout_payload in response_data.get("data", []):
            checkouts.append(Checkout(**checkout_payload))

        meta = response_data.get("meta", {}).get("page", {})
        if page >= meta.get("lastPage", 1):
            break
        page += 1

    return checkouts


__all__ = ["get_checkout", "list_checkouts"]
