"""
A price object represents a price added to a Variant.
When a variant’s price is changed a new price object is created. All old prices are retained.
A price belongs to a Variant and can have many Subscription Items and Usage records.

{
  "type": "prices",
  "id": "1",
  "attributes": {
    "variant_id": 1,
    "category": "subscription",
    "scheme": "graduated",
    "usage_aggregation": null,
    "unit_price": 999,
    "unit_price_decimal": null,
    "setup_fee_enabled": false,
    "setup_fee": null,
    "package_size": 1,
    "tiers": [
      {
        "last_unit": 2,
        "unit_price": 10000,
        "unit_price_decimal": null,
        "fixed_fee": 1000
      },
      {
        "last_unit": "inf",
        "unit_price": 1000,
        "unit_price_decimal": null,
        "fixed_fee": 1000
      }
    ],
    "renewal_interval_unit": "year",
    "renewal_interval_quantity": 1,
    "trial_interval_unit": "day",
    "trial_interval_quantity": 30,
    "min_price": null,
    "suggested_price": null,
    "tax_code": "eservice",
    "created_at": "2023-05-24T14:15:06.000000Z",
    "updated_at": "2023-06-24T14:44:38.000000Z"
  }
}

"""

from typing import Optional

from pydantic import BaseModel, Field

from lemonsqueezy.models import BaseEntity


class _Price(BaseEntity):
    """A price object represents a price added to a Variant."""

    class Attributes(BaseModel):
        """The attributes of a Price object"""

        class Tier(BaseModel):
            """The price tiers for this price"""

            last_unit: str
            unit_price: int
            unit_price_decimal: Optional[int]
            fixed_fee: int

        variant_id: int
        category: str
        scheme: str
        usage_aggregation: Optional[str]
        unit_price: int
        unit_price_decimal: Optional[int]
        setup_fee_enabled: Optional[bool]
        setup_fee: Optional[int]
        package_size: int
        tiers: Optional[list[Tier]]
        renewal_interval_unit: Optional[str]
        renewal_interval_quantity: Optional[int]
        trial_interval_unit: Optional[str]
        trial_interval_quantity: Optional[int]
        min_price: Optional[int]
        suggested_price: Optional[int]
        tax_code: str
        created_at: str
        updated_at: str

    attributes: Attributes


class Price(_Price):
    class Relationships(BaseModel):
        class Variant(BaseModel):
            class Links(BaseModel):
                related: str
                self_: str = Field(..., alias="self")

            links: Links

        variant: Variant

    class Links(BaseModel):
        self_: str = Field(..., alias="self")

    relationships: Relationships
    links: Links
