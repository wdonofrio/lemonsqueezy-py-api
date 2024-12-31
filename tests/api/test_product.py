from lemonsqueezy.api.product import get_product, list_products
from lemonsqueezy.models.product import Product


def test_get_product(client, product_id) -> None:
    product = get_product(client, product_id)
    assert isinstance(product, Product)


def test_list_products(client) -> None:
    products = list_products(client)
    assert all(isinstance(product, Product) for product in products)
