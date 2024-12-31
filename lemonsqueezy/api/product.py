import requests

from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.product import Product
from lemonsqueezy.models.variant import Variant
from lemonsqueezy.protocols import LemonSqueezyProtocol


@handle_http_errors
def get_product(client: LemonSqueezyProtocol, product_id: str | int) -> Product:
    """Get the product"""
    response = requests.get(
        f"{client.base_url}/products/{product_id}",
        headers=client.headers,
        timeout=30,
    )
    response.raise_for_status()
    product_data = response.json().get("data", {})
    return Product(**product_data)


@handle_http_errors
def get_product_variants(
    client: LemonSqueezyProtocol, product_id: str | int
) -> list[Variant]:
    """Get the product variants"""
    response = requests.get(
        f"{client.base_url}/products/{product_id}/variants",
        headers=client.headers,
        timeout=30,
    )
    response.raise_for_status()
    response_data = response.json()
    return [Variant(**variant_data) for variant_data in response_data.get("data", [])]


def list_products(
    client: LemonSqueezyProtocol, page: int = 1, per_page: int = 10
) -> list[Product]:
    """List the customers with pagination"""
    products = []
    while True:
        response = requests.get(
            f"{client.base_url}/products?page[number]={page}&page[size]={per_page}",
            headers=client.headers,
            timeout=30,
        )
        response.raise_for_status()
        response_data = response.json()

        for product_data in response_data.get("data", []):
            products.append(Product(**product_data))

        meta = response_data.get("meta", {}).get("page", {})
        if page >= meta.get("lastPage", 1):
            break
        page += 1

    return products
