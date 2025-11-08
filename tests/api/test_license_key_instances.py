from lemonsqueezy.api.license_key_instances import (
    get_license_key_instance,
    list_license_key_instances,
)
from lemonsqueezy.models.license_key_instance import LicenseKeyInstance


def test_get_license_key_instance(client, license_key_instance_id):
    instance = get_license_key_instance(client, license_key_instance_id)
    assert isinstance(instance, LicenseKeyInstance)


def test_list_license_key_instances(client):
    instances = list_license_key_instances(client)
    assert all(isinstance(instance, LicenseKeyInstance) for instance in instances)
