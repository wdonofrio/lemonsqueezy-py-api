"""Agent covering the `/license-keys` endpoints."""

import requests

from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.license_key import LicenseKey, LicenseKeyUpdate
from lemonsqueezy.protocols import LemonSqueezyProtocol


@handle_http_errors
def get_license_key(
    client: LemonSqueezyProtocol, license_key_id: str | int
) -> LicenseKey:
    """Retrieve a single license key."""
    response = requests.get(
        f"{client.base_url}/license-keys/{license_key_id}",
        headers=client.headers,
        timeout=30,
    )
    response.raise_for_status()
    license_key_data = response.json().get("data", {})
    return LicenseKey(**license_key_data)


@handle_http_errors
def update_license_key(
    client: LemonSqueezyProtocol, payload: LicenseKeyUpdate
) -> LicenseKey:
    """Update mutable license key attributes such as limits or expiration."""
    license_key_id = payload.data.model_dump(by_alias=True).get("id")
    if not license_key_id:
        raise ValueError("License key ID is required in the update payload.")

    # Serialize while excluding None values (applies recursively to nested models)
    json_payload = payload.model_dump(by_alias=True, exclude_none=True)

    response = requests.patch(
        f"{client.base_url}/license-keys/{license_key_id}",
        headers=client.headers,
        json=json_payload,
        timeout=30,
    )
    response.raise_for_status()
    license_key_data = response.json().get("data", {})
    return LicenseKey(**license_key_data)


@handle_http_errors
def list_license_keys(
    client: LemonSqueezyProtocol, page: int = 1, per_page: int = 10
) -> list[LicenseKey]:
    """List license keys with pagination."""
    license_keys: list[LicenseKey] = []
    while True:
        response = requests.get(
            f"{client.base_url}/license-keys?page[number]={page}&page[size]={per_page}",
            headers=client.headers,
            timeout=30,
        )
        response.raise_for_status()
        response_data = response.json()
        license_keys.extend(
            LicenseKey(**payload) for payload in response_data.get("data", [])
        )

        meta = response_data.get("meta", {}).get("page", {})
        if page >= meta.get("lastPage", 1):
            break
        page += 1

    return license_keys
