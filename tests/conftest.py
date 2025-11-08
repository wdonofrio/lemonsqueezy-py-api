from random import random

import pytest

from lemonsqueezy.api.customer import list_customers
from lemonsqueezy.api.file import list_files
from lemonsqueezy.api.license_key_instances import list_license_key_instances
from lemonsqueezy.api.license_keys import list_license_keys
from lemonsqueezy.api.order import list_orders
from lemonsqueezy.api.prices import list_prices
from lemonsqueezy.api.product import list_products
from lemonsqueezy.api.subscription import list_subscriptions
from lemonsqueezy.api.subscription_invoices import list_subscription_invoices
from lemonsqueezy.api.subscription_items import list_subscription_items
from lemonsqueezy.api.store import list_stores
from lemonsqueezy.api.variant import list_variants
from lemonsqueezy.client import LemonSqueezy


@pytest.fixture
def client():
    return LemonSqueezy()


@pytest.fixture
def store_id(client):
    stores = list_stores(client)
    assert stores != [], "No stores available."
    return stores[int(random() * len(stores))].id_


@pytest.fixture
def customer_id(client):
    customers = list_customers(client)
    assert customers != [], "No customers available."
    return customers[int(random() * len(customers))].id_


@pytest.fixture
def product_id(client):
    products = list_products(client)
    assert products != [], "No products available."
    return products[int(random() * len(products))].id_


@pytest.fixture
def variant_id(client):
    variants = list_variants(client)
    assert variants != [], "No variants available."
    return variants[int(random() * len(variants))].id_


@pytest.fixture
def price_id(client):
    prices = list_prices(client)
    assert prices != [], "No prices available."
    return prices[int(random() * len(prices))].id_


@pytest.fixture
def file_id(client):
    files = list_files(client)
    assert files != [], "No files available."
    return files[int(random() * len(files))].id_


@pytest.fixture
def order_id(client):
    orders = list_orders(client)
    if not orders:
        pytest.skip("No orders available.")
    return orders[int(random() * len(orders))].id_


@pytest.fixture
def license_key_id(client):
    license_keys = list_license_keys(client)
    if not license_keys:
        pytest.skip("No license keys available.")
    return license_keys[int(random() * len(license_keys))].id_


@pytest.fixture
def license_key_instance_id(client):
    instances = list_license_key_instances(client)
    if not instances:
        pytest.skip("No license key instances available.")
    return instances[int(random() * len(instances))].id_


@pytest.fixture
def subscription_id(client):
    subscriptions = list_subscriptions(client)
    if not subscriptions:
        pytest.skip("No subscriptions available.")
    return subscriptions[int(random() * len(subscriptions))].id_


@pytest.fixture
def subscription_item_id(client):
    subscription_items = list_subscription_items(client)
    if not subscription_items:
        pytest.skip("No subscription items available.")
    return subscription_items[int(random() * len(subscription_items))].id_


@pytest.fixture
def subscription_invoice_id(client):
    subscription_invoices = list_subscription_invoices(client)
    if not subscription_invoices:
        pytest.skip("No subscription invoices available.")
    return subscription_invoices[int(random() * len(subscription_invoices))].id_
