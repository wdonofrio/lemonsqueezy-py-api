from lemonsqueezy.client import LemonSqueezy
from lemonsqueezy.models.customer import Customer
from lemonsqueezy.models.file import File
from lemonsqueezy.models.license_api import LicenseValidationResponse
from lemonsqueezy.models.license_key import LicenseKey
from lemonsqueezy.models.license_key_instance import LicenseKeyInstance
from lemonsqueezy.models.product import Product
from lemonsqueezy.models.store import Store
from lemonsqueezy.models.subscription import Subscription
from lemonsqueezy.models.subscription_invoice import SubscriptionInvoice
from lemonsqueezy.models.subscription_item import SubscriptionItem
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


def test_get_license_key(client: LemonSqueezy, license_key_id):
    license_key = client.get_license_key(license_key_id)
    assert isinstance(license_key, LicenseKey)


def test_list_license_keys(client: LemonSqueezy):
    license_keys = client.list_license_keys()
    assert all(isinstance(license_key, LicenseKey) for license_key in license_keys)


def test_get_license_key_instance(client: LemonSqueezy, license_key_instance_id):
    instance = client.get_license_key_instance(license_key_instance_id)
    assert isinstance(instance, LicenseKeyInstance)


def test_list_license_key_instances(client: LemonSqueezy):
    instances = client.list_license_key_instances()
    assert all(isinstance(instance, LicenseKeyInstance) for instance in instances)


def test_validate_license_key(client: LemonSqueezy, license_key_id):
    license_key = client.get_license_key(license_key_id)
    validation = client.validate_license_key(license_key.attributes.key)
    assert isinstance(validation, LicenseValidationResponse)


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


def test_get_subscription(client: LemonSqueezy, subscription_id):
    subscription = client.get_subscription(subscription_id)
    assert isinstance(subscription, Subscription)


def test_list_subscriptions(client: LemonSqueezy):
    subscriptions = client.list_subscriptions()
    assert all(isinstance(subscription, Subscription) for subscription in subscriptions)


def test_get_subscription_item(client: LemonSqueezy, subscription_item_id):
    subscription_item = client.get_subscription_item(subscription_item_id)
    assert isinstance(subscription_item, SubscriptionItem)


def test_list_subscription_items(client: LemonSqueezy):
    subscription_items = client.list_subscription_items()
    assert all(
        isinstance(subscription_item, SubscriptionItem)
        for subscription_item in subscription_items
    )


def test_get_subscription_invoice(client: LemonSqueezy, subscription_invoice_id):
    subscription_invoice = client.get_subscription_invoice(subscription_invoice_id)
    assert isinstance(subscription_invoice, SubscriptionInvoice)


def test_list_subscription_invoices(client: LemonSqueezy):
    subscription_invoices = client.list_subscription_invoices()
    assert all(
        isinstance(subscription_invoice, SubscriptionInvoice)
        for subscription_invoice in subscription_invoices
    )
