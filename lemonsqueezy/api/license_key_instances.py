"""Agent for `/license-key-instances`."""

import requests

from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.license_key_instance import LicenseKeyInstance
from lemonsqueezy.protocols import LemonSqueezyProtocol


@handle_http_errors
def get_license_key_instance(
    client: LemonSqueezyProtocol, instance_id: str | int
) -> LicenseKeyInstance:
    """Retrieve a single license key instance."""
    response = requests.get(
        f"{client.base_url}/license-key-instances/{instance_id}",
        headers=client.headers,
        timeout=30,
    )
    response.raise_for_status()
    instance_data = response.json().get("data", {})
    return LicenseKeyInstance(**instance_data)


@handle_http_errors
def list_license_key_instances(
    client: LemonSqueezyProtocol, page: int = 1, per_page: int = 10
) -> list[LicenseKeyInstance]:
    """List license key instances with pagination."""
    instances: list[LicenseKeyInstance] = []
    while True:
        response = requests.get(
            f"{client.base_url}/license-key-instances?page[number]={page}&page[size]={per_page}",
            headers=client.headers,
            timeout=30,
        )
        response.raise_for_status()
        response_data = response.json()
        instances.extend(
            LicenseKeyInstance(**payload) for payload in response_data.get("data", [])
        )

        meta = response_data.get("meta", {}).get("page", {})
        if page >= meta.get("lastPage", 1):
            break
        page += 1

    return instances
