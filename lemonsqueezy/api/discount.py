import requests

from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.discount import Discount
from lemonsqueezy.protocols import LemonSqueezyProtocol


@handle_http_errors
def get_discount(client: LemonSqueezyProtocol, discount_id: str | int) -> Discount:
    """Fetch a single discount."""
    response = requests.get(
        f"{client.base_url}/discounts/{discount_id}",
        headers=client.headers,
        timeout=30,
    )
    response.raise_for_status()
    discount_data = response.json().get("data", {})
    return Discount(**discount_data)


@handle_http_errors
def list_discounts(
    client: LemonSqueezyProtocol, page: int = 1, per_page: int = 10
) -> list[Discount]:
    """Paginate through all discounts."""
    discounts: list[Discount] = []
    while True:
        response = requests.get(
            f"{client.base_url}/discounts?page[number]={page}&page[size]={per_page}",
            headers=client.headers,
            timeout=30,
        )
        response.raise_for_status()
        response_data = response.json()

        for discount_payload in response_data.get("data", []):
            discounts.append(Discount(**discount_payload))

        meta = response_data.get("meta", {}).get("page", {})
        if page >= meta.get("lastPage", 1):
            break
        page += 1

    return discounts


__all__ = ["get_discount", "list_discounts"]
