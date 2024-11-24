import requests

from lemonsqueezy.api import BASE_URL, get_headers
from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.prices import Price


@handle_http_errors
def get_price(price_id: str | int) -> Price:
    """Get the Price"""
    response = requests.get(
        f"{BASE_URL}/prices/{price_id}", headers=get_headers(), timeout=30
    )
    response.raise_for_status()
    price_data = response.json().get("data", {})
    return Price(**price_data)


@handle_http_errors
def list_prices() -> list[Price]:
    """List the Prices"""
    prices = []
    page = 1
    while True:
        response = requests.get(
            f"{BASE_URL}/prices?page[number]={page}&page[size]=10",
            headers=get_headers(),
            timeout=30,
        )
        response.raise_for_status()
        response_data = response.json()

        for price_data in response_data.get("data", []):
            prices.append(Price(**price_data))

        meta = response_data.get("meta", {}).get("page", {})
        if page >= meta.get("lastPage", 1):
            break
        page += 1

    return prices
