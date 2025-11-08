"""The Discount Redemption Object:
https://docs.lemonsqueezy.com/api/discount-redemptions/the-discount-redemption-object
Represents the usage of a discount against a specific order.
"""

from __future__ import annotations

from pydantic import BaseModel

from lemonsqueezy.models import BaseEntity


class DiscountRedemption(BaseEntity):
    """The Discount Redemption Object"""

    class Attributes(BaseModel):
        """The Attributes sub-object in the Discount Redemption Object"""

        discount_id: int
        order_id: int
        discount_name: str
        discount_code: str
        discount_amount: int
        discount_amount_type: str
        amount: int
        created_at: str
        updated_at: str

    attributes: Attributes


__all__ = ["DiscountRedemption"]
