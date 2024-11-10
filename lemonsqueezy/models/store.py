"""The Store Object: https://docs.lemonsqueezy.com/api/stores/the-store-object
Everything in Lemon Squeezy belongs to a store. Each store is billed separately.

{
  "type": "stores",
  "id": "1",
  "attributes": {
    "name": "My Store",
    "slug": "my-store",
    "domain": "my-store.lemonsqueezy.com",
    "url": "https://my-store.lemonsqueezy.com",
    "avatar_url": "https://app.lemonsqueezy.com/storage/avatars/stores/1/czTkMkDm4Vfb8PZehb5c29XFCm9JZyJx0AjEZP7s.png",
    "plan": "fresh",
    "country": "US",
    "country_nicename": "United States",
    "currency": "USD",
    "total_sales": 1,
    "total_revenue": 999,
    "thirty_day_sales": 0,
    "thirty_day_revenue": 0,
    "created_at": "2024-05-24T14:15:06.000000Z",
    "updated_at": "2024-06-15T10:03:14.000000Z"
  }
}

"""

from pydantic import BaseModel

from lemonsqueezy.models import BaseEntity


class Store(BaseEntity):
    """The Store Object"""

    class Attributes(BaseModel):
        """The Attributes sub-object in the Store Object"""

        name: str
        slug: str
        domain: str
        url: str
        avatar_url: str
        plan: str
        country: str
        country_nicename: str
        currency: str
        total_sales: int
        total_revenue: int
        thirty_day_sales: int
        thirty_day_revenue: int
        created_at: str
        updated_at: str

    attributes: Attributes
