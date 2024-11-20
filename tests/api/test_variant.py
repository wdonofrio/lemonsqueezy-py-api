from lemonsqueezy.api.variant import get_variant, list_variants
from lemonsqueezy.models.variant import Variant


def test_get_variant(variant_id):
    variant = get_variant(variant_id)
    assert isinstance(variant, Variant)


def test_list_variants():
    variants = list_variants()
    assert all(isinstance(variant, Variant) for variant in variants)
