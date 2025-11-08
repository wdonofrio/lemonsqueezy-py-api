"""Models for `/license-key-instances`."""

from pydantic import BaseModel, Field

from lemonsqueezy.models import BaseEntity


class Links(BaseModel):
    """Relationship links shared across nested objects."""

    related: str
    self_: str = Field(..., alias="self")


class LicenseKeyInstance(BaseEntity):
    """Represents a single license key activation/instance."""

    class Attributes(BaseModel):
        license_key_id: int
        identifier: str
        name: str | None = None
        created_at: str
        updated_at: str

    class Relationships(BaseModel):
        class LicenseKey(BaseModel):
            links: Links

        license_key: LicenseKey = Field(..., alias="license-key")

    class Links_(BaseModel):
        self_: str = Field(..., alias="self")

    attributes: Attributes
    relationships: Relationships | None = None
    links: Links_ | None = None
