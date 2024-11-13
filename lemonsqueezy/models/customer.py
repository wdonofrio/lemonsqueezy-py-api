"""The Customer Object: https://docs.lemonsqueezy.com/api/customers/the-customer-object
A customer object represents a customer of your store. It is created when they purchase a product for the first time.

{
  "type": "customers",
  "id": "1",
  "attributes": {
    "store_id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com",
    "status": "subscribed",
    "city": null,
    "region": null,
    "country": "US",
    "total_revenue_currency": 84332,
    "mrr": 1999,
    "status_formatted": "Subscribed",
    "country_formatted": "United States",
    "total_revenue_currency_formatted": "$843.32",
    "mrr_formatted": "$19.99",
    "urls": {
      "customer_portal": "https://my-store.lemonsqueezy.com/billing?expires=1666869343&signature=82ae290ceac8edd4190c82825dd73a8743346d894a8ddbc4898b97eb96d105a5"
    },
    "created_at": "2022-12-01T13:01:07.000000Z",
    "updated_at": "2022-12-09T09:05:21.000000Z",
    "test_mode": false
  }
}

"""

from typing import Optional

from pydantic import BaseModel, Field

from lemonsqueezy.models import BaseEntity


class Customer(BaseEntity):
    """The Store Object"""

    class Attributes(BaseModel):
        """The Attributes sub-object in the Customer Object"""

        class URLs(BaseModel):
            """The URLs sub-object in the Attributes sub-object"""

            customer_portal: Optional[str]

        store_id: int
        name: str
        email: str
        status: str
        city: str
        region: str
        country: str
        total_revenue_currency: int
        mrr: int
        status_formatted: str
        country_formatted: str
        total_revenue_currency_formatted: str
        mrr_formatted: str
        urls: URLs
        created_at: str
        updated_at: str
        test_mode: bool

    attributes: Attributes


class CustomerCreate(BaseModel):
    """The Customer Object for creating a new customer"""

    class Data(BaseModel):
        """The Data sub-object in the Customer Object"""

        class Attributes(BaseModel):
            """The Attributes sub-object in the Customer Object"""

            name: str
            email: str
            city: str
            region: str
            country: str

        class Relationships(BaseModel):
            """The Relationships sub-object in the Customer Object"""

            class Store(BaseModel):
                """The Store sub-object in the Relationships sub-object"""

                class StoreData(BaseModel):
                    """The Data sub-object in the Relationships sub-object"""

                    type_: str = Field(..., alias="type")
                    id: str

                data: StoreData

            store: Store

        type_: str = Field(..., alias="type")
        attributes: Attributes
        relationships: Relationships

    data: Data


class CustomerPatch(BaseModel):
    """The Customer Object for updating a customer"""

    class Data(BaseEntity):
        """The Data sub-object in the Customer Object"""

        class Attributes(BaseModel):
            """The Attributes sub-object in the Customer Object"""

            name: str
            email: str
            status: str

        attributes: Attributes

    data: Data


class Links(BaseModel):
    """The Links sub-object"""

    related: str
    self_: str = Field(..., alias="self")


class CustomerList(Customer):
    """The Customer List Object"""

    class Relationships(BaseModel):
        """The Relationships sub-object in the Customer List Object"""

        class Store(BaseModel):
            """The Store sub-object in the Relationships sub-object"""

            links: Links

        class Orders(BaseModel):
            """The Orders sub-object in the Relationships Object"""

            links: Links

        class Subscriptions(BaseModel):
            """The Subscriptions sub-object in the Relationships Object"""

            links: Links

        class LicenseKeys(BaseModel):
            """The LicenseKeys sub-object in the Relationships Object"""

            links: Links

        store: Store
        orders: Orders
        subscriptions: Subscriptions
        license_keys: LicenseKeys  #  = Field(..., alias="license-keys")

    class Links_(BaseModel):
        """The Links sub-object in the Customer List Object"""

        self_: str = Field(..., alias="self")

    relationships: Relationships
    links: Links_
