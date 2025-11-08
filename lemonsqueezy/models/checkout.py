"""The Checkout Object: https://docs.lemonsqueezy.com/api/checkouts/the-checkout-object
A checkout represents a custom checkout page for selling a specific product or
variant while overriding presentation, pricing, or pre-filled buyer data.

{
    "type": "checkouts",
    "id": "ac470bd4-7c41-474d-b6cd-0f296f5be02a",
    "attributes": {
      "store_id": 1,
      "variant_id": 1,
      "custom_price": null,
      "product_options": {
        "name": "",
        "description": "",
        "media": [],
        "redirect_url": "",
        "receipt_button_text": "",
        "receipt_link_url": "",
        "receipt_thank_you_note": "",
        "enabled_variants": []
      },
      "checkout_options": {
        "embed": false,
        "media": true,
        "logo": true,
        "desc": true,
        "discount": true,
        "skip_trial": false,
        "subscription_preview": true,
        "button_color": "#7047EB"
      },
      "checkout_data": {
        "email": "",
        "name": "",
        "billing_address": [],
        "tax_number": "",
        "discount_code": "",
        "custom": [],
        "variant_quantities": []
      },
      "expires_at": null,
      "created_at": "2024-10-14T12:36:27.000000Z",
      "updated_at": "2024-10-14T12:36:27.000000Z",
      "test_mode": false,
      "url": "https://my-store.lemonsqueezy.com/checkout/custom/ac470bd4-7c41-474d-b6cd-0f296f5be02a"
    }
}
"""

from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field

from lemonsqueezy.models import BaseEntity


class Checkout(BaseEntity):
    """The Checkout Object"""

    class Attributes(BaseModel):
        """The Attributes sub-object in the Checkout Object"""

        class ProductOptions(BaseModel):
            """Overrides for the product presentation on the checkout page."""

            name: str
            description: str
            media: list[str]
            redirect_url: str
            receipt_button_text: str
            receipt_link_url: str
            receipt_thank_you_note: str
            enabled_variants: list[int]

        class CheckoutOptions(BaseModel):
            """Visual and behavioral controls for the hosted checkout."""

            embed: bool
            media: bool
            logo: bool
            desc: bool
            discount: bool
            skip_trial: bool
            subscription_preview: bool
            button_color: str

        class CheckoutData(BaseModel):
            """Prefilled customer data for the checkout form."""

            email: str
            name: str
            billing_address: dict[str, Any] | list[Any]
            tax_number: str
            discount_code: str
            custom: list[Any]
            variant_quantities: list[Any]

        class Preview(BaseModel):
            """Pricing preview returned when `preview=true` is set."""

            currency: str
            currency_rate: float
            subtotal: int
            discount_total: int
            tax: int
            total: int
            subtotal_usd: int
            discount_total_usd: int
            tax_usd: int
            total_usd: int
            subtotal_formatted: str
            discount_total_formatted: str
            tax_formatted: str
            total_formatted: str

        store_id: int
        variant_id: int
        custom_price: Optional[int]
        product_options: ProductOptions
        checkout_options: CheckoutOptions
        checkout_data: CheckoutData
        expires_at: Optional[str]
        created_at: str
        updated_at: str
        test_mode: bool
        url: str
        preview: Optional[Preview] = None

    class Relationships(BaseModel):
        """Relationships included with the Checkout object."""

        class Links(BaseModel):
            related: str
            self_: str = Field(..., alias="self")

        class Store(BaseModel):
            links: "Checkout.Relationships.Links"

        class Variant(BaseModel):
            links: "Checkout.Relationships.Links"

        store: Store
        variant: Variant

    class Links(BaseModel):
        """The Links sub-object in the Checkout Object"""

        self_: str = Field(..., alias="self")

    attributes: Attributes
    relationships: Relationships
    links: Links


__all__ = ["Checkout"]
