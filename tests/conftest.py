from random import random

import pytest

from lemonsqueezy.api.customer import list_customers
from lemonsqueezy.api.file import list_files
from lemonsqueezy.api.prices import list_prices
from lemonsqueezy.api.product import list_products
from lemonsqueezy.api.store import list_stores
from lemonsqueezy.api.variant import list_variants


@pytest.fixture
def store_id():
    stores = list_stores()
    assert stores != [], "No stores available."
    return stores[int(random() * len(stores))].id_


@pytest.fixture
def customer_id():
    customers = list_customers()
    assert customers != [], "No customers available."
    return customers[int(random() * len(customers))].id_


@pytest.fixture
def product_id():
    products = list_products()
    assert products != [], "No products available."
    return products[int(random() * len(products))].id_


@pytest.fixture
def variant_id():
    variants = list_variants()
    assert variants != [], "No variants available."
    return variants[int(random() * len(variants))].id_


@pytest.fixture
def price_id():
    prices = list_prices()
    assert prices != [], "No prices available."
    return prices[int(random() * len(prices))].id_


@pytest.fixture
def file_id():
    files = list_files()
    assert files != [], "No files available."
    return files[int(random() * len(files))].id_
