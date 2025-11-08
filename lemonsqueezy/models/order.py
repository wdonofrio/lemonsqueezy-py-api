"""The Order Object: https://docs.lemonsqueezy.com/api/orders/the-order-object
An order is created when a customer purchases a product. Orders belong to a store,
are associated with a customer, and reference order items, subscriptions, license
keys, and discount redemptions.
"""

from typing import Optional

from pydantic import BaseModel, Field

from lemonsqueezy.models import BaseEntity


class Links(BaseModel):
    """Reusable links structure used across relationships."""

    related: str
    self_: str = Field(..., alias="self")


class _Order(BaseEntity):
    """Represents the core order payload returned by the API."""

    class Attributes(BaseModel):
        """Top-level order attributes."""

        class OrderItem(BaseModel):
            """Denormalized view of the first order item."""

            id: int
            order_id: int
            product_id: int
            variant_id: int
            product_name: str
            variant_name: str
            price: int
            created_at: str
            updated_at: str
            test_mode: bool

        class URLs(BaseModel):
            """Links related to the order."""

            receipt: str

        store_id: int
        customer_id: int
        identifier: str
        order_number: int
        user_name: str
        user_email: str
        currency: str
        currency_rate: str
        subtotal: int
        setup_fee: Optional[int]
        discount_total: int
        tax: int
        total: int
        subtotal_usd: int
        setup_fee_usd: Optional[int]
        discount_total_usd: int
        tax_usd: int
        total_usd: int
        tax_name: Optional[str]
        tax_rate: Optional[str]
        tax_inclusive: bool
        status: str
        status_formatted: str
        refunded: bool
        refunded_at: Optional[str]
        subtotal_formatted: str
        setup_fee_formatted: Optional[str]
        discount_total_formatted: str
        tax_formatted: str
        total_formatted: str
        first_order_item: Optional[OrderItem]
        urls: URLs
        created_at: str
        updated_at: str
        test_mode: bool

    attributes: Attributes


class Order(_Order):
    """Order object with relationships and top-level links."""

    class Relationships(BaseModel):
        class Store(BaseModel):
            links: Links

        class Customer(BaseModel):
            links: Links

        class OrderItems(BaseModel):
            links: Links

        class Subscriptions(BaseModel):
            links: Links

        class LicenseKeys(BaseModel):
            links: Links

        class DiscountRedemptions(BaseModel):
            links: Links

        store: Store
        customer: Customer
        order_items: OrderItems = Field(..., alias="order-items")
        subscriptions: Subscriptions
        license_keys: LicenseKeys = Field(..., alias="license-keys")
        discount_redemptions: DiscountRedemptions = Field(
            ..., alias="discount-redemptions"
        )

    class Links(BaseModel):
        self_: str = Field(..., alias="self")

    relationships: Relationships
    links: Links
