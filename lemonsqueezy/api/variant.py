import requests

from lemonsqueezy.api import BASE_URL, get_headers
from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.variant import Variant


@handle_http_errors
def get_variant(variant_id: str | int) -> Variant:
    """Get the variant"""
    response = requests.get(
        f"{BASE_URL}/variants/{variant_id}", headers=get_headers(), timeout=30
    )
    response.raise_for_status()
    variant_data = response.json().get("data", {})
    return Variant(**variant_data)


@handle_http_errors
def list_variants(page: int = 1, per_page: int = 10) -> list[Variant]:
    """List the variants with pagination"""
    variants = []
    while True:
        response = requests.get(
            f"{BASE_URL}/variants?page[number]={page}&page[size]={per_page}",
            headers=get_headers(),
            timeout=30,
        )
        response.raise_for_status()
        response_data = response.json()

        for variant_data in response_data.get("data", []):
            variants.append(Variant(**variant_data))

        meta = response_data.get("meta", {}).get("page", {})
        if page >= meta.get("lastPage", 1):
            break
        page += 1

    return variants
