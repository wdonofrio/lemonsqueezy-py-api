import requests

from lemonsqueezy.config import settings
from lemonsqueezy.models import User

BASE_URL = "https://api.lemonsqueezy.com/v1/"


def get_headers() -> dict:
    """Get the headers for the request"""
    return {
        "Accept": "application/vnd.api+json",
        "Content-Type": "application/vnd.api+json",
        "Authorization": f"Bearer {settings.api_key}",
    }


def get_user():
    """Get the user"""
    response = requests.get(f"{BASE_URL}/users/me", headers=get_headers())
    response.raise_for_status()
    user_data = response.json().get("data", {})
    return User(**user_data)


def get_store(store_id: str):
    """Get the store"""
    raise NotImplementedError


def list_stores():
    """List the stores"""
    raise NotImplementedError


def create_customer():
    """Create a customer"""
    raise NotImplementedError


def get_customer(customer_id: str):
    """Get a customer"""
    raise NotImplementedError


def update_customer(customer_id: str):
    """Update a customer"""
    raise NotImplementedError


def list_customers():
    """List the customers"""
    raise NotImplementedError


def get_product(product_id: str):
    """Get a product"""
    raise NotImplementedError


def list_products():
    """List the products"""
    raise NotImplementedError


def get_variant(variant_id: str):
    """Get a variant"""
    raise NotImplementedError


def list_variants():
    """List the variants"""
    raise NotImplementedError


def get_price(price_id: str):
    """Get a price"""
    raise NotImplementedError


def list_prices():
    """List the prices"""
    raise NotImplementedError


def get_file(file_id: str):
    """Get a file"""
    raise NotImplementedError


def list_files():
    """List the files"""
    raise NotImplementedError


def get_order(order_id: str):
    """Get an order"""
    raise NotImplementedError


def list_orders():
    """List the orders"""
    raise NotImplementedError


def generate_order_invoice(order_id: str):
    """Generate an invoice for an order"""
    raise NotImplementedError


def issue_refund_order(order_id: str):
    """Issue a refund for an order"""
    raise NotImplementedError


def get_order_item(order_item_id: str):
    """Get an order item"""
    raise NotImplementedError


def list_order_items():
    """List the order items"""
    raise NotImplementedError


def update_subscription(subscription_id: str):
    """Update a subscription"""
    raise NotImplementedError


def retrieve_subscription(subscription_id: str):
    """Retrieve a subscription"""
    raise NotImplementedError


def list_subscriptions():
    """List the subscriptions"""
    raise NotImplementedError


def cancel_subscription(subscription_id: str):
    """Cancel a subscription"""
    raise NotImplementedError


def get_subscription_invoice(subscription_id: str):
    """Get a subscription invoice"""
    raise NotImplementedError


def list_subscription_invoices():
    """List the subscription invoices"""
    raise NotImplementedError


def generate_subscription_invoice(subscription_id: str):
    """Generate an invoice for a subscription"""
    raise NotImplementedError


def issue_refund_subscription(subscription_id: str):
    """Issue a refund for a subscription"""
    raise NotImplementedError


def get_subscription_item(subscription_item_id: str):
    """Get a subscription item"""
    raise NotImplementedError


def get_subscription_item_usage(subscription_item_id: str):
    """Get the usage for a subscription item"""
    raise NotImplementedError


def update_subscription_item(subscription_item_id: str):
    """Update a subscription item"""
    raise NotImplementedError


def list_subscription_items():
    """List the subscription items"""
    raise NotImplementedError


def create_usage_record(subscription_item_id: str):
    """Create a usage record"""
    raise NotImplementedError


def get_usage_record(usage_record_id: str):
    """Get a usage record"""
    raise NotImplementedError


def list_usage_records():
    """List the usage records"""
    raise NotImplementedError


def create_discount():
    """Create a discount"""
    raise NotImplementedError


def get_discount(discount_id: str):
    """Get a discount"""
    raise NotImplementedError


def delete_discount(discount_id: str):
    """Delete a discount"""
    raise NotImplementedError


def list_discounts():
    """List the discounts"""
    raise NotImplementedError


def get_discount_redemption(discount_redemption_id: str):
    """Get a discount redemption"""
    raise NotImplementedError


def list_discount_redemptions():
    """List the discount redemptions"""
    raise NotImplementedError


def get_license_key(license_key_id: str):
    """Get a license key"""
    raise NotImplementedError


def update_license_key(license_key_id: str):
    """Update a license key"""
    raise NotImplementedError


def list_license_keys():
    """List the license keys"""
    raise NotImplementedError


def get_license_key_instance(license_key_instance_id: str):
    """Get a license key instance"""
    raise NotImplementedError


def list_license_key_instances():
    """List the license key instances"""
    raise NotImplementedError


def create_checkout():
    """Create a checkout"""
    raise NotImplementedError


def get_checkout(checkout_id: str):
    """Get a checkout"""
    raise NotImplementedError


def list_checkouts():
    """List the checkouts"""
    raise NotImplementedError


def create_webhook():
    """Create a webhook"""
    raise NotImplementedError


def retrieve_webhook(webhook_id: str):
    """Retrieve a webhook"""
    raise NotImplementedError


def update_webhook(webhook_id: str):
    """Update a webhook"""
    raise NotImplementedError


def delete_webhook(webhook_id: str):
    """Delete a webhook"""
    raise NotImplementedError


def list_webhooks():
    """List the webhooks"""
    raise NotImplementedError


def activate_license_key(license_key_id: str):
    """Activate a license key"""
    raise NotImplementedError


def deactivate_license_key(license_key_id: str):
    """Deactivate a license key"""
    raise NotImplementedError


def validate_license_key(license_key_id: str):
    """Validate a license key"""
    raise NotImplementedError
