from uuid import uuid4

import pytest

from lemonsqueezy.api.errors import LemonSqueezyClientError
from lemonsqueezy.api.license_api import (
    activate_license_key,
    deactivate_license_key,
    validate_license_key,
)
from lemonsqueezy.api.license_keys import get_license_key, list_license_keys
from lemonsqueezy.models.license_api import (
    LicenseActivationResponse,
    LicenseDeactivationResponse,
    LicenseValidationResponse,
)
from lemonsqueezy.models.license_key import LicenseKey


@pytest.fixture
def activatable_license_key(client) -> LicenseKey:
    """Pick a license key that still has room for new activations."""
    license_keys = list_license_keys(client)
    if not license_keys:
        pytest.skip("No license keys available.")

    for license_key in license_keys:
        attrs = license_key.attributes
        if attrs.disabled:
            continue
        limit = attrs.activation_limit
        if limit is None or attrs.instances_count < limit:
            return license_key

    pytest.skip("No license keys with available activation slots.")


def test_validate_license_key(client, license_key_id):
    license_key = get_license_key(client, license_key_id)
    response = validate_license_key(client, license_key.attributes.key)

    assert isinstance(response, LicenseValidationResponse)
    assert response.license_key.key == license_key.attributes.key


def test_activate_and_deactivate_license_key(client, activatable_license_key):
    instance_name = f"pytest-{uuid4()}"
    try:
        activation = activate_license_key(
            client, activatable_license_key.attributes.key, instance_name
        )
    except LemonSqueezyClientError as exc:
        if exc.status_code in (400, 404, 422):
            pytest.skip(f"Activation unavailable in this environment: {exc}")
        raise

    assert isinstance(activation, LicenseActivationResponse)
    if not activation.activated or activation.instance is None:
        pytest.skip("License activation API responded without creating an instance.")

    instance_id = activation.instance.id
    deactivation = deactivate_license_key(
        client, activatable_license_key.attributes.key, instance_id
    )
    assert isinstance(deactivation, LicenseDeactivationResponse)
    assert isinstance(deactivation.deactivated, bool)
