"""Models backing the Lemon Squeezy license key endpoints."""

from pydantic import BaseModel, Field

from lemonsqueezy.models import BaseEntity


class Links(BaseModel):
    """Reusable relationship links structure."""

    related: str
    self_: str = Field(..., alias="self")


class LicenseKey(BaseEntity):
    """Represents the `/license-keys` resource."""

    class Attributes(BaseModel):
        store_id: int
        customer_id: int
        order_id: int
        order_item_id: int
        product_id: int
        variant_id: int | None = None
        user_name: str | None = None
        user_email: str | None = None
        key: str
        key_short: str
        activation_limit: int | None = None
        instances_count: int
        disabled: bool
        status: str
        status_formatted: str
        expires_at: str | None = None
        created_at: str
        updated_at: str
        test_mode: bool

    class Relationships(BaseModel):
        class Store(BaseModel):
            links: Links

        class Customer(BaseModel):
            links: Links

        class Order(BaseModel):
            links: Links

        class OrderItem(BaseModel):
            links: Links

        class Product(BaseModel):
            links: Links

        class Variant(BaseModel):
            links: Links

        class LicenseKeyInstances(BaseModel):
            links: Links

        store: Store
        customer: Customer
        order: Order
        order_item: OrderItem = Field(..., alias="order-item")
        product: Product
        variant: Variant
        license_key_instances: LicenseKeyInstances = Field(
            ..., alias="license-key-instances"
        )

    class Links_(BaseModel):
        self_: str = Field(..., alias="self")

    attributes: Attributes
    relationships: Relationships
    links: Links_


class LicenseKeyUpdate(BaseModel):
    """Payload builder for PATCH /license-keys/:id."""

    class Data(BaseEntity):
        class Attributes(BaseModel):
            activation_limit: int | None = None
            expires_at: str | None = None
            disabled: bool | None = None

        attributes: Attributes

    data: Data
