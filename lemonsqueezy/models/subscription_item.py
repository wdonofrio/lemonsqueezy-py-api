"""The Subscription Item Object: https://docs.lemonsqueezy.com/api/subscriptions/the-subscription-item-object
Subscription items describe the individual prices that make up a subscription.
"""

from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

from lemonsqueezy.models import BaseEntity


class RelationshipLinks(BaseModel):
    """Shared representation of relationship link payloads."""

    related: str
    self_: str = Field(..., alias="self")


class _SubscriptionItem(BaseEntity):
    """Core Subscription Item representation."""

    class Attributes(BaseModel):
        """Attributes exposed for subscription items."""

        model_config = ConfigDict(extra="allow")

        subscription_id: int
        price_id: int
        quantity: int
        is_usage_based: bool
        usage_limit: Optional[int] = None
        created_at: str
        updated_at: str
        test_mode: bool

    attributes: Attributes


class SubscriptionItem(_SubscriptionItem):
    """Subscription Item including relationships."""

    class Relationships(BaseModel):
        """Linked resources for the item."""

        model_config = ConfigDict(extra="allow")

        class Subscription(BaseModel):
            links: RelationshipLinks

        class Price(BaseModel):
            links: RelationshipLinks

        class OrderItem(BaseModel):
            links: RelationshipLinks

        class Product(BaseModel):
            links: RelationshipLinks

        class Variant(BaseModel):
            links: RelationshipLinks

        subscription: Optional[Subscription] = None
        price: Optional[Price] = None
        order_item: Optional[OrderItem] = Field(default=None, alias="order-item")
        product: Optional[Product] = None
        variant: Optional[Variant] = None

    class Links(BaseModel):
        """Top-level links block."""

        self_: str = Field(..., alias="self")

    relationships: Relationships
    links: Links


__all__ = ["SubscriptionItem"]
