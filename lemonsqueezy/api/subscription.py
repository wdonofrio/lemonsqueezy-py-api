import requests

from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.subscription import Subscription
from lemonsqueezy.protocols import LemonSqueezyProtocol


@handle_http_errors
def get_subscription(
    client: LemonSqueezyProtocol, subscription_id: str | int
) -> Subscription:
    """Retrieve a single subscription by ID."""
    response = requests.get(
        f"{client.base_url}/subscriptions/{subscription_id}",
        headers=client.headers,
        timeout=30,
    )
    response.raise_for_status()
    subscription_data = response.json().get("data", {})
    return Subscription(**subscription_data)


@handle_http_errors
def list_subscriptions(
    client: LemonSqueezyProtocol, page: int = 1, per_page: int = 10
) -> list[Subscription]:
    """List subscriptions, exhausting pagination to return the complete collection."""
    subscriptions: list[Subscription] = []
    while True:
        response = requests.get(
            f"{client.base_url}/subscriptions?page[number]={page}&page[size]={per_page}",
            headers=client.headers,
            timeout=30,
        )
        response.raise_for_status()
        response_data = response.json()
        subscriptions.extend(
            Subscription(**subscription_data)
            for subscription_data in response_data.get("data", [])
        )

        meta = response_data.get("meta", {}).get("page", {})
        if page >= meta.get("lastPage", 1):
            break
        page += 1

    return subscriptions
