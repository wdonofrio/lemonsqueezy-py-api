import requests

from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.subscription_item import SubscriptionItem
from lemonsqueezy.protocols import LemonSqueezyProtocol


@handle_http_errors
def get_subscription_item(
    client: LemonSqueezyProtocol, subscription_item_id: str | int
) -> SubscriptionItem:
    """Retrieve a subscription item by ID."""
    response = requests.get(
        f"{client.base_url}/subscription-items/{subscription_item_id}",
        headers=client.headers,
        timeout=30,
    )
    response.raise_for_status()
    item_data = response.json().get("data", {})
    return SubscriptionItem(**item_data)


@handle_http_errors
def list_subscription_items(
    client: LemonSqueezyProtocol, page: int = 1, per_page: int = 10
) -> list[SubscriptionItem]:
    """List subscription items with pagination."""
    items: list[SubscriptionItem] = []
    while True:
        response = requests.get(
            f"{client.base_url}/subscription-items?page[number]={page}&page[size]={per_page}",
            headers=client.headers,
            timeout=30,
        )
        response.raise_for_status()
        response_data = response.json()
        items.extend(
            SubscriptionItem(**item_data) for item_data in response_data.get("data", [])
        )

        meta = response_data.get("meta", {}).get("page", {})
        if page >= meta.get("lastPage", 1):
            break
        page += 1

    return items
