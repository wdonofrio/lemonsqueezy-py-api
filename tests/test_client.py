from lemonsqueezy.client import LemonSqueezy
from lemonsqueezy.models.customer import Customer
from lemonsqueezy.models.file import File
from lemonsqueezy.models.product import Product
from lemonsqueezy.models.store import Store
from lemonsqueezy.models.variant import Variant


def test_client_api_privacy(client: LemonSqueezy):
    """Test that the API key and URL are not exposed"""
    assert not hasattr(client, "api_key")
    assert not hasattr(client, "api_url")


def test_list_stores(client: LemonSqueezy):
    stores = client.list_stores()
    assert all(isinstance(store, Store) for store in stores)


def test_list_customers(client: LemonSqueezy):
    customers = client.list_customers()
    assert all(isinstance(customer, Customer) for customer in customers)


def test_get_product(client: LemonSqueezy, product_id):
    product = client.get_product(product_id)
    assert isinstance(product, Product)


def test_get_product_variants(client: LemonSqueezy, product_id):
    variants = client.get_product_variants(product_id)
    assert all(isinstance(variant, Variant) for variant in variants)


def test_list_products(client: LemonSqueezy):
    products = client.list_products()
    assert all(isinstance(product, Product) for product in products)


def test_get_file(client: LemonSqueezy, file_id):
    file = client.get_file(file_id)
    assert isinstance(file, File)


def test_list_files(client: LemonSqueezy):
    files = client.list_files()
    assert all(isinstance(file, File) for file in files)


def test_get_variant(client: LemonSqueezy, variant_id):
    variant = client.get_variant(variant_id)
    assert isinstance(variant, Variant)


def test_list_variants(client: LemonSqueezy):
    variants = client.list_variants()
    assert all(isinstance(variant, Variant) for variant in variants)
