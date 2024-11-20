from lemonsqueezy.api.product import get_product, list_products
from lemonsqueezy.models.product import Product


def test_get_product(product_id) -> None:
    product = get_product(product_id)
    assert isinstance(product, Product)


def test_list_products() -> None:
    products = list_products()
    assert all(isinstance(product, Product) for product in products)
