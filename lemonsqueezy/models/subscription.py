"""The Subscription Object: https://docs.lemonsqueezy.com/api/subscriptions/the-subscription-object
A subscription is created when a subscription product is purchased. It bills the customer on a recurring basis.
"""

from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

from lemonsqueezy.models import BaseEntity


class RelationshipLinks(BaseModel):
    """Reusable representation of relationship link payloads."""

    related: str
    self_: str = Field(..., alias="self")


class _Subscription(BaseEntity):
    """Base Subscription object without relationships."""

    class Attributes(BaseModel):
        """Top-level subscription fields."""

        model_config = ConfigDict(extra="allow")

        class Pause(BaseModel):
            """Pause configuration for the subscription."""

            model_config = ConfigDict(extra="allow")

            behavior: Optional[str] = Field(default=None, alias="behavior")
            resumes_at: Optional[str] = Field(default=None, alias="resumes_at")

        class URLs(BaseModel):
            """Convenient links exposed by the API."""

            model_config = ConfigDict(extra="allow")

            update_payment_method: Optional[str] = None
            customer_portal: Optional[str] = None

        store_id: int
        customer_id: int
        order_id: int
        order_item_id: int
        product_id: int
        variant_id: int
        product_name: str
        variant_name: str
        user_name: str
        user_email: str
        status: str
        status_formatted: str
        card_brand: Optional[str] = None
        card_last_four: Optional[str] = None
        card_exp_month: Optional[int] = None
        card_exp_year: Optional[int] = None
        billing_anchor: Optional[int] = None
        trial_ends_at: Optional[str] = None
        renews_at: Optional[str] = None
        ends_at: Optional[str] = None
        cancelled: bool
        cancelled_at: Optional[str] = None
        pause: Optional[Pause] = None
        urls: URLs
        created_at: str
        updated_at: str
        test_mode: bool

    attributes: Attributes


class Subscription(_Subscription):
    """Subscription containing relationship and link metadata."""

    class Relationships(BaseModel):
        """Linked resources for the subscription."""

        model_config = ConfigDict(extra="allow")

        class Store(BaseModel):
            links: RelationshipLinks

        class Customer(BaseModel):
            links: RelationshipLinks

        class Order(BaseModel):
            links: RelationshipLinks

        class OrderItem(BaseModel):
            links: RelationshipLinks

        class Product(BaseModel):
            links: RelationshipLinks

        class Variant(BaseModel):
            links: RelationshipLinks

        class SubscriptionItems(BaseModel):
            links: RelationshipLinks

        class SubscriptionInvoices(BaseModel):
            links: RelationshipLinks

        store: Optional[Store] = None
        customer: Optional[Customer] = None
        order: Optional[Order] = None
        order_item: Optional[OrderItem] = Field(default=None, alias="order-item")
        product: Optional[Product] = None
        variant: Optional[Variant] = None
        subscription_items: Optional[SubscriptionItems] = Field(
            default=None, alias="subscription-items"
        )
        subscription_invoices: Optional[SubscriptionInvoices] = Field(
            default=None, alias="subscription-invoices"
        )

    class Links(BaseModel):
        """Top-level links block."""

        self_: str = Field(..., alias="self")

    relationships: Relationships
    links: Links


__all__ = ["Subscription"]
