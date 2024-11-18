import requests

from lemonsqueezy.api import BASE_URL, get_headers
from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.store import Store


@handle_http_errors
def get_store(store_id: str | int) -> Store:
    """Get the store"""
    response = requests.get(
        f"{BASE_URL}/stores/{store_id}", headers=get_headers(), timeout=30
    )
    response.raise_for_status()
    store_data = response.json().get("data", {})
    return Store(**store_data)


@handle_http_errors
def list_stores() -> list[Store]:
    """List the stores"""
    response = requests.get(f"{BASE_URL}/stores", headers=get_headers(), timeout=30)
    response.raise_for_status()
    stores_data = response.json().get("data", [])
    return [Store(**store_data) for store_data in stores_data]
