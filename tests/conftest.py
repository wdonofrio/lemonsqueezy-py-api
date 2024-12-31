from random import random

import pytest

from lemonsqueezy.api.customer import list_customers
from lemonsqueezy.api.file import list_files
from lemonsqueezy.api.prices import list_prices
from lemonsqueezy.api.product import list_products
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
