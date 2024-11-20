import requests

from lemonsqueezy.api import BASE_URL, get_headers
from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.product import Product


@handle_http_errors
def get_product(product_id: str | int) -> Product:
    """Get the product"""
    response = requests.get(
        f"{BASE_URL}/products/{product_id}", headers=get_headers(), timeout=30
    )
    response.raise_for_status()
    product_data = response.json().get("data", {})
    return Product(**product_data)


def list_products(page: int = 1, per_page: int = 10) -> list[Product]:
    """List the customers with pagination"""
    products = []
    while True:
        response = requests.get(
            f"{BASE_URL}/products?page[number]={page}&page[size]={per_page}",
            headers=get_headers(),
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
