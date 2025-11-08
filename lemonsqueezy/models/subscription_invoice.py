"""The Subscription Invoice Object: https://docs.lemonsqueezy.com/api/subscriptions/the-subscription-invoice-object
Invoices capture the billing events for a subscription.
"""

from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

from lemonsqueezy.models import BaseEntity


class RelationshipLinks(BaseModel):
    """Shared representation of relationship link payloads."""

    related: str
    self_: str = Field(..., alias="self")


class _SubscriptionInvoice(BaseEntity):
    """Core invoice representation."""

    class Attributes(BaseModel):
        """Invoice attributes."""

        model_config = ConfigDict(extra="allow")

        class URLs(BaseModel):
            """Convenient URLs for invoice downloads."""

            model_config = ConfigDict(extra="allow")

            invoice_url: Optional[str] = None
            pdf: Optional[str] = None
            receipt: Optional[str] = None

        store_id: int
        subscription_id: int
        order_id: int
        customer_id: int
        status: str
        status_formatted: str
        invoice_number: str
        currency: str
        subtotal: int
        discount_total: Optional[int] = None
        tax: int
        total: int
        subtotal_formatted: str
        discount_total_formatted: Optional[str] = None
        tax_formatted: str
        total_formatted: str
        refunded: bool
        refunded_at: Optional[str] = None
        due_at: Optional[str] = None
        paid_at: Optional[str] = None
        urls: URLs
        created_at: str
        updated_at: str
        test_mode: bool

    attributes: Attributes


class SubscriptionInvoice(_SubscriptionInvoice):
    """Invoice enriched with relationship metadata."""

    class Relationships(BaseModel):
        """Linked resources for the invoice."""

        model_config = ConfigDict(extra="allow")

        class Store(BaseModel):
            links: RelationshipLinks

        class Subscription(BaseModel):
            links: RelationshipLinks

        class Order(BaseModel):
            links: RelationshipLinks

        class Customer(BaseModel):
            links: RelationshipLinks

        store: Optional[Store] = None
        subscription: Optional[Subscription] = None
        order: Optional[Order] = None
        customer: Optional[Customer] = None

    class Links(BaseModel):
        """Top-level links block."""

        self_: str = Field(..., alias="self")

    relationships: Relationships
    links: Links


__all__ = ["SubscriptionInvoice"]
