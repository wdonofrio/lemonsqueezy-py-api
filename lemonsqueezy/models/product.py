"""The Product Object: https://docs.lemonsqueezy.com/api/products/the-product-object
Products describe digital goods you offer to your customers.

{
  "type": "products",
  "id": "1",
  "attributes": {
    "store_id": 1,
    "name": "Example Product",
    "slug": "example-product",
    "description": "<p>Lorem ipsum...</p>",
    "status": "published",
    "status_formatted": "Published",
    "thumb_url": "https://app.lemonsqueezy.com/storage/media/1/1c40f227-aed5-4321-9ffc-62f37a06c9a0.jpg",
    "large_thumb_url": "https://app.lemonsqueezy.com/storage/media/1/1c40f227-aed5-4321-9ffc-62f37a06c9a0.jpg",
    "price": 999,
    "price_formatted": "$9.99",
    "from_price": null,
    "to_price": null,
    "pay_what_you_want": false,
    "buy_now_url": "https://my-store.lemonsqueezy.com/checkout/buy/0a841cf5-4cc2-4bbb-ae5d-9529d97deec6",
    "from_price_formatted": null,
    "to_price_formatted": null,
    "created_at": "2021-05-27T12:54:47.000000Z",
    "updated_at": "2021-07-14T11:25:24.000000Z",
    "test_mode": false
  }
}


"""

from pydantic import BaseModel

from lemonsqueezy.models import BaseEntity


class Product(BaseEntity):
    """The Product Object"""

    class Attributes(BaseModel):
        """The Attributes sub-object in the Product Object"""

        store_id: int
        name: str
        slug: str
        description: str
        status: str
        status_formatted: str
        thumb_url: str
        large_thumb_url: str
        price: int
        price_formatted: str
        from_price: int
        to_price: int
        pay_what_you_want: bool
        buy_now_url: str
        from_price_formatted: str
        to_price_formatted: str
        created_at: str
        updated_at: str
        test_mode: bool

    attributes: Attributes
