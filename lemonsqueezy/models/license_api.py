"""Models for the standalone license activation/validation endpoints."""

from pydantic import BaseModel


class LicenseMeta(BaseModel):
    store_id: int | None = None
    order_id: int | None = None
    order_item_id: int | None = None
    product_id: int | None = None
    product_name: str | None = None
    variant_id: int | None = None
    variant_name: str | None = None
    customer_id: int | None = None
    customer_name: str | None = None
    customer_email: str | None = None


class LicenseApiLicenseKey(BaseModel):
    id: int
    status: str
    key: str
    activation_limit: int | None = None
    activation_usage: int | None = None
    created_at: str
    expires_at: str | None = None


class LicenseApiInstance(BaseModel):
    id: str
    name: str
    created_at: str


class LicenseActivationResponse(BaseModel):
    activated: bool
    error: str | None = None
    license_key: LicenseApiLicenseKey
    instance: LicenseApiInstance | None = None
    meta: LicenseMeta


class LicenseDeactivationResponse(BaseModel):
    deactivated: bool
    error: str | None = None
    license_key: LicenseApiLicenseKey
    meta: LicenseMeta


class LicenseValidationResponse(BaseModel):
    valid: bool
    error: str | None = None
    license_key: LicenseApiLicenseKey
    instance: LicenseApiInstance | None = None
    meta: LicenseMeta
