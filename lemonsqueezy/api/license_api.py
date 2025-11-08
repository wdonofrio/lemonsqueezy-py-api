"""Wrappers for the standalone license activation endpoints."""

import requests

from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.license_api import (
    LicenseActivationResponse,
    LicenseDeactivationResponse,
    LicenseValidationResponse,
)
from lemonsqueezy.protocols import LemonSqueezyProtocol


def _license_api_headers(client: LemonSqueezyProtocol) -> dict[str, str]:
    """The license API expects standard JSON headers instead of JSON:API ones."""
    auth_header = client.headers.get("Authorization")
    if auth_header is None:
        msg = "Lemon Squeezy client is missing the Authorization header"
        raise ValueError(msg)
    return {
        "Accept": "application/json",
        "Authorization": auth_header,
    }


@handle_http_errors
def activate_license_key(
    client: LemonSqueezyProtocol, license_key: str, instance_name: str
) -> LicenseActivationResponse:
    """Activate (create) a new license key instance."""
    response = requests.post(
        f"{client.base_url}/licenses/activate",
        headers=_license_api_headers(client),
        data={"license_key": license_key, "instance_name": instance_name},
        timeout=30,
    )
    response.raise_for_status()
    return LicenseActivationResponse(**response.json())


@handle_http_errors
def deactivate_license_key(
    client: LemonSqueezyProtocol, license_key: str, instance_id: str
) -> LicenseDeactivationResponse:
    """Deactivate an existing license key instance."""
    response = requests.post(
        f"{client.base_url}/licenses/deactivate",
        headers=_license_api_headers(client),
        data={"license_key": license_key, "instance_id": instance_id},
        timeout=30,
    )
    response.raise_for_status()
    return LicenseDeactivationResponse(**response.json())


@handle_http_errors
def validate_license_key(
    client: LemonSqueezyProtocol, license_key: str, instance_id: str | None = None
) -> LicenseValidationResponse:
    """Validate a license key (or a specific instance)."""
    payload: dict[str, str] = {"license_key": license_key}
    if instance_id:
        payload["instance_id"] = instance_id

    response = requests.post(
        f"{client.base_url}/licenses/validate",
        headers=_license_api_headers(client),
        data=payload,
        timeout=30,
    )
    response.raise_for_status()
    return LicenseValidationResponse(**response.json())
