from lemonsqueezy.api.variant import get_variant, list_variants
from lemonsqueezy.models.variant import Variant


def test_get_variant(client, variant_id):
    variant = get_variant(client, variant_id)
    assert isinstance(variant, Variant)


def test_list_variants(client):
    variants = list_variants(client)
    assert all(isinstance(variant, Variant) for variant in variants)
