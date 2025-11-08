import requests

from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.order import Order
from lemonsqueezy.protocols import LemonSqueezyProtocol


@handle_http_errors
def get_order(client: LemonSqueezyProtocol, order_id: str | int) -> Order:
    """Retrieve a single order by ID."""
    response = requests.get(
        f"{client.base_url}/orders/{order_id}", headers=client.headers, timeout=30
    )
    response.raise_for_status()
    order_data = response.json().get("data", {})
    return Order(**order_data)


@handle_http_errors
def list_orders(
    client: LemonSqueezyProtocol, page: int = 1, per_page: int = 10
) -> list[Order]:
    """List orders, exhausting pagination to return the full collection."""
    orders: list[Order] = []
    while True:
        response = requests.get(
            f"{client.base_url}/orders?page[number]={page}&page[size]={per_page}",
            headers=client.headers,
            timeout=30,
        )
        response.raise_for_status()
        response_data = response.json()
        orders.extend(
            Order(**order_data) for order_data in response_data.get("data", [])
        )

        meta = response_data.get("meta", {}).get("page", {})
        if page >= meta.get("lastPage", 1):
            break
        page += 1

    return orders
