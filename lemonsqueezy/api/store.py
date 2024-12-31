import requests

from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.store import Store
from lemonsqueezy.protocols import LemonSqueezyProtocol


@handle_http_errors
def get_store(client: LemonSqueezyProtocol, store_id: str | int) -> Store:
    """Get the store"""
    response = requests.get(
        f"{client.base_url}/stores/{store_id}", headers=client.headers, timeout=30
    )
    response.raise_for_status()
    store_data = response.json().get("data", {})
    return Store(**store_data)


@handle_http_errors
def list_stores(client: LemonSqueezyProtocol) -> list[Store]:
    """List the stores"""
    response = requests.get(
        f"{client.base_url}/stores", headers=client.headers, timeout=30
    )
    response.raise_for_status()
    stores_data = response.json().get("data", [])
    return [Store(**store_data) for store_data in stores_data]
