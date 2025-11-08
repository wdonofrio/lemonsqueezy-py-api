import requests

from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.discount_redemption import DiscountRedemption
from lemonsqueezy.protocols import LemonSqueezyProtocol


@handle_http_errors
def get_discount_redemption(
    client: LemonSqueezyProtocol, redemption_id: str | int
) -> DiscountRedemption:
    """Fetch a single discount redemption."""
    response = requests.get(
        f"{client.base_url}/discount-redemptions/{redemption_id}",
        headers=client.headers,
        timeout=30,
    )
    response.raise_for_status()
    redemption_data = response.json().get("data", {})
    return DiscountRedemption(**redemption_data)


@handle_http_errors
def list_discount_redemptions(
    client: LemonSqueezyProtocol, page: int = 1, per_page: int = 10
) -> list[DiscountRedemption]:
    """Paginate through discount redemptions."""
    redemptions: list[DiscountRedemption] = []
    while True:
        response = requests.get(
            f"{client.base_url}/discount-redemptions?page[number]={page}&page[size]={per_page}",
            headers=client.headers,
            timeout=30,
        )
        response.raise_for_status()
        response_data = response.json()

        for redemption_payload in response_data.get("data", []):
            redemptions.append(DiscountRedemption(**redemption_payload))

        meta = response_data.get("meta", {}).get("page", {})
        if page >= meta.get("lastPage", 1):
            break
        page += 1

    return redemptions


__all__ = ["get_discount_redemption", "list_discount_redemptions"]
