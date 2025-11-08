from lemonsqueezy.api.license_keys import (
    get_license_key,
    list_license_keys,
    update_license_key,
)
from lemonsqueezy.models.license_key import LicenseKey, LicenseKeyUpdate


def test_get_license_key(client, license_key_id):
    license_key = get_license_key(client, license_key_id)
    assert isinstance(license_key, LicenseKey)


def test_list_license_keys(client):
    license_keys = list_license_keys(client)
    assert all(isinstance(license_key, LicenseKey) for license_key in license_keys)


def test_update_license_key_noop(client, license_key_id):
    """Send a no-op update to ensure the PATCH helper is wired."""
    license_key = get_license_key(client, license_key_id)
    payload = LicenseKeyUpdate(
        data=LicenseKeyUpdate.Data(
            type="license-keys",
            id=license_key_id,
            attributes=LicenseKeyUpdate.Data.Attributes(
                activation_limit=license_key.attributes.activation_limit,
                expires_at=license_key.attributes.expires_at,
                disabled=license_key.attributes.disabled,
            ),
        )
    )

    updated_license_key = update_license_key(client, payload)
    assert isinstance(updated_license_key, LicenseKey)
