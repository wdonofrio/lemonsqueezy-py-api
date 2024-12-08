from lemonsqueezy import LemonSqueezy
from lemonsqueezy.config import settings
from lemonsqueezy.models.customer import Customer
from lemonsqueezy.models.file import File
from lemonsqueezy.models.product import Product
from lemonsqueezy.models.store import Store
from lemonsqueezy.models.variant import Variant

client = LemonSqueezy(api_key=settings.api_key, api_url=settings.api_url)


def test_list_stores():
    stores = client.list_stores()
    assert all(isinstance(store, Store) for store in stores)


def test_list_customers():
    customers = client.list_customers()
    assert all(isinstance(customer, Customer) for customer in customers)


def test_get_product(product_id):
    product = client.get_product(product_id)
    assert isinstance(product, Product)


def test_get_product_variants(product_id):
    variants = client.get_product_variants(product_id)
    assert all(isinstance(variant, Variant) for variant in variants)


def test_list_products():
    products = client.list_products()
    assert all(isinstance(product, Product) for product in products)


def test_get_file(file_id):
    file = client.get_file(file_id)
    assert isinstance(file, File)


def test_list_files():
    files = client.list_files()
    assert all(isinstance(file, File) for file in files)


def test_get_variant(variant_id):
    variant = client.get_variant(variant_id)
    assert isinstance(variant, Variant)


def test_list_variants():
    variants = client.list_variants()
    assert all(isinstance(variant, Variant) for variant in variants)
