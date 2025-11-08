"""The Discount Object: https://docs.lemonsqueezy.com/api/discounts/the-discount-object
Discounts are promotional codes that can be restricted by date, usage, or product.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel

from lemonsqueezy.models import BaseEntity


class Discount(BaseEntity):
    """The Discount Object"""

    class Attributes(BaseModel):
        """The Attributes sub-object in the Discount Object"""

        store_id: int
        name: str
        code: str
        amount: int
        amount_type: str
        is_limited_to_products: bool
        is_limited_redemptions: bool
        max_redemptions: int
        starts_at: Optional[str]
        expires_at: Optional[str]
        duration: str
        duration_in_months: Optional[int]
        status: str
        status_formatted: str
        created_at: str
        updated_at: str
        test_mode: bool

    attributes: Attributes


__all__ = ["Discount"]
