"""The Variant Object: https://docs.lemonsqueezy.com/api/products/the-variant-object
A variant represents a variation of a Product, with its own set of pricing options, files and license key settings.

{
  "type": "variants",
  "id": "1",
  "attributes": {
    "product_id": 1,
    "name": "Example Variant",
    "slug": "46beb127-a8a9-33e6-89b5-078505657239",
    "description": "<p>Lorem ipsum...</p>",
    "price": 999,
    "is_subscription": false,
    "interval": null,
    "interval_count": null,
    "has_free_trial": false,
    "trial_interval": "day",
    "trial_interval_count": 30,
    "pay_what_you_want": false,
    "min_price": 0,
    "suggested_price": 0,
    "has_license_keys": false,
    "license_activation_limit": 5,
    "is_license_limit_unlimited": false,
    "license_length_value": 1,
    "license_length_unit": "years",
    "is_license_length_unlimited": false,
    "sort": 1,
    "status": "published",
    "status_formatted": "Published",
    "created_at": "2021-05-24T14:15:06.000000Z",
    "updated_at": "2021-06-24T14:44:38.000000Z",
    "test_mode": false
  }
}

"""

from pydantic import BaseModel

from lemonsqueezy.models import BaseEntity


class Attributes(BaseModel):
    """The Attributes sub-object in the Variant Object"""

    product_id: int
    name: str
    slug: str
    description: str
    price: int
    is_subscription: bool
    interval: str
    interval_count: int
    has_free_trial: bool
    trial_interval: str
    trial_interval_count: int
    pay_what_you_want: bool
    min_price: int
    suggested_price: int
    has_license_keys: bool
    license_activation_limit: int
    is_license_limit_unlimited: bool
    license_length_value: int
    license_length_unit: str
    is_license_length_unlimited: bool
    sort: int
    status: str
    status_formatted: str
    created_at: str
    updated_at: str
    test_mode: bool


class Variant(BaseEntity):
    """The Variant Object"""

    class Attributes(BaseModel):
        """The Attributes sub-object in the Variant Object"""

        product_id: int
        name: str
        slug: str
        description: str
        price: int
        is_subscription: bool
        interval: str
        interval_count: int
        has_free_trial: bool
        trial_interval: str
        trial_interval_count: int
        pay_what_you_want: bool
        min_price: int
        suggested_price: int
        has_license_keys: bool
        license_activation_limit: int
        is_license_limit_unlimited: bool
        license_length_value: int
        license_length_unit: str
        is_license_length_unlimited: bool
        sort: int
        status: str
        status_formatted: str
        created_at: str
        updated_at: str
        test_mode: bool

    attributes: Attributes
