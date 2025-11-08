import os
from typing import Optional

from lemonsqueezy.api.checkout import get_checkout, list_checkouts
from lemonsqueezy.api.customer import list_customers
from lemonsqueezy.api.discount import get_discount, list_discounts
from lemonsqueezy.api.discount_redemption import (
    get_discount_redemption,
    list_discount_redemptions,
)
from lemonsqueezy.api.file import get_file, list_files
from lemonsqueezy.api.license_api import (
    activate_license_key as activate_license_key_api,
    deactivate_license_key as deactivate_license_key_api,
    validate_license_key as validate_license_key_api,
)
from lemonsqueezy.api.license_key_instances import (
    get_license_key_instance,
    list_license_key_instances,
)
from lemonsqueezy.api.license_keys import (
    get_license_key,
    list_license_keys,
    update_license_key,
)
from lemonsqueezy.api.order import get_order, list_orders
from lemonsqueezy.api.prices import get_price, list_prices
from lemonsqueezy.api.product import get_product, get_product_variants, list_products
from lemonsqueezy.api.subscription import get_subscription, list_subscriptions
from lemonsqueezy.api.subscription_invoices import (
    get_subscription_invoice,
    list_subscription_invoices,
)
from lemonsqueezy.api.subscription_items import (
    get_subscription_item,
    list_subscription_items,
)
from lemonsqueezy.api.store import list_stores
from lemonsqueezy.api.user import get_user
from lemonsqueezy.api.variant import get_variant, list_variants
from lemonsqueezy.models.checkout import Checkout
from lemonsqueezy.models.customer import Customer
from lemonsqueezy.models.discount import Discount
from lemonsqueezy.models.discount_redemption import DiscountRedemption
from lemonsqueezy.models.file import File
from lemonsqueezy.models.license_api import (
    LicenseActivationResponse,
    LicenseDeactivationResponse,
    LicenseValidationResponse,
)
from lemonsqueezy.models.license_key import LicenseKey, LicenseKeyUpdate
from lemonsqueezy.models.license_key_instance import LicenseKeyInstance
from lemonsqueezy.models.order import Order
from lemonsqueezy.models.prices import Price
from lemonsqueezy.models.product import Product
from lemonsqueezy.models.subscription import Subscription
from lemonsqueezy.models.subscription_invoice import SubscriptionInvoice
from lemonsqueezy.models.subscription_item import SubscriptionItem
from lemonsqueezy.models.store import Store
from lemonsqueezy.models.user import User
from lemonsqueezy.models.variant import Variant
from lemonsqueezy.protocols import LemonSqueezyProtocol


class LemonSqueezy(LemonSqueezyProtocol):
    """LemonSqueezy API client"""

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_url: Optional[str] = None,
    ):
        """
        Initialize the LemonSqueezy client.

        Args:
            api_key (Optional[str]): The API key for authentication. Defaults to environment variable LEMONSQUEEZY_API_KEY.
            api_url (Optional[str]): The base URL for the API. Defaults to environment variable LEMONSQUEEZY_API_URL or the official API URL.

        Raises:
            ValueError: If the API key is not provided and not found in the environment variable.
        """
        self.__api_key = api_key or self._get_default_api_key()
        if not self.__api_key:
            raise ValueError(
                "API key is required. Provide it as an argument or set LEMONSQUEEZY_API_KEY in the environment."
            )

        self.__api_url = api_url or self._get_default_api_url()
        if not self.__api_url:
            raise ValueError(
                "API URL is required. Provide it as an argument or set LEMONSQUEEZY_API_URL in the environment."
            )

    @staticmethod
    def _get_default_api_key() -> Optional[str]:
        """Retrieve the default API key from the environment."""
        return os.getenv("LEMONSQUEEZY_API_KEY")

    @staticmethod
    def _get_default_api_url() -> str:
        """Retrieve the default API URL from the environment."""
        return os.getenv("LEMONSQUEEZY_API_URL", "https://api.lemonsqueezy.com/v1")

    @property
    def headers(self) -> dict[str, str]:
        """Get the headers for the request"""
        return {
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json",
            "Authorization": f"Bearer {self.__api_key}",
        }

    @property
    def base_url(self) -> str:
        """Return the base URL for the API"""
        return self.__api_url

    def list_stores(self) -> list[Store]:
        return list_stores(self)

    def list_customers(self) -> list[Customer]:
        return list_customers(self)

    def get_license_key(self, license_key_id: str | int) -> LicenseKey:
        return get_license_key(self, license_key_id)

    def list_license_keys(self) -> list[LicenseKey]:
        return list_license_keys(self)

    def update_license_key(self, payload: LicenseKeyUpdate) -> LicenseKey:
        return update_license_key(self, payload)

    def get_license_key_instance(self, instance_id: str | int) -> LicenseKeyInstance:
        return get_license_key_instance(self, instance_id)

    def list_license_key_instances(self) -> list[LicenseKeyInstance]:
        return list_license_key_instances(self)

    def activate_license_key(
        self, license_key: str, instance_name: str
    ) -> LicenseActivationResponse:
        return activate_license_key_api(self, license_key, instance_name)

    def deactivate_license_key(
        self, license_key: str, instance_id: str
    ) -> LicenseDeactivationResponse:
        return deactivate_license_key_api(self, license_key, instance_id)

    def validate_license_key(
        self, license_key: str, instance_id: str | None = None
    ) -> LicenseValidationResponse:
        return validate_license_key_api(self, license_key, instance_id)

    def get_checkout(self, checkout_id: str) -> Checkout:
        return get_checkout(self, checkout_id)

    def list_checkouts(self) -> list[Checkout]:
        return list_checkouts(self)

    def get_discount(self, discount_id: str | int) -> Discount:
        return get_discount(self, discount_id)

    def list_discounts(self) -> list[Discount]:
        return list_discounts(self)

    def get_discount_redemption(self, redemption_id: str | int) -> DiscountRedemption:
        return get_discount_redemption(self, redemption_id)

    def list_discount_redemptions(self) -> list[DiscountRedemption]:
        return list_discount_redemptions(self)

    def get_order(self, order_id: str | int) -> Order:
        return get_order(self, order_id)

    def list_orders(self) -> list[Order]:
        return list_orders(self)

    def get_product(self, product_id: str | int) -> Product:
        return get_product(self, product_id)

    def get_product_variants(self, product_id: str | int) -> list[Product]:
        return get_product_variants(self, product_id)

    def list_products(self) -> list[Product]:
        return list_products(self)

    def get_file(self, file_id: str | int) -> File:
        return get_file(self, file_id)

    def list_files(self) -> list[File]:
        return list_files(self)

    def get_price(self, price_id: str | int) -> Price:
        return get_price(self, price_id)

    def list_prices(self) -> list[Price]:
        return list_prices(self)

    def get_variant(self, variant_id: str | int) -> Product:
        return get_variant(self, variant_id)

    def list_variants(self) -> list[Variant]:
        return list_variants(self)

    def get_subscription(self, subscription_id: str | int) -> Subscription:
        return get_subscription(self, subscription_id)

    def list_subscriptions(self) -> list[Subscription]:
        return list_subscriptions(self)

    def get_subscription_item(
        self, subscription_item_id: str | int
    ) -> SubscriptionItem:
        return get_subscription_item(self, subscription_item_id)

    def list_subscription_items(self) -> list[SubscriptionItem]:
        return list_subscription_items(self)

    def get_subscription_invoice(
        self, subscription_invoice_id: str | int
    ) -> SubscriptionInvoice:
        return get_subscription_invoice(self, subscription_invoice_id)

    def list_subscription_invoices(self) -> list[SubscriptionInvoice]:
        return list_subscription_invoices(self)

    def get_user(self) -> User:
        return get_user(self)
