import pytest
import requests

from lemonsqueezy.api import checkout as checkout_api
from lemonsqueezy.api.checkout import get_checkout, list_checkouts
from lemonsqueezy.api.errors import LemonSqueezyClientError
from lemonsqueezy.models.checkout import Checkout

MOCK_CHECKOUT = {
    "type": "checkouts",
    "id": "ac470bd4-7c41-474d-b6cd-0f296f5be02a",
    "attributes": {
        "store_id": 1,
        "variant_id": 1,
        "custom_price": None,
        "product_options": {
            "name": "Custom checkout",
            "description": "A custom experience",
            "media": [],
            "redirect_url": "https://lemonsqueezy.com",
            "receipt_button_text": "Download",
            "receipt_link_url": "https://lemonsqueezy.com/download",
            "receipt_thank_you_note": "Enjoy!",
            "enabled_variants": [],
        },
        "checkout_options": {
            "embed": False,
            "media": True,
            "logo": True,
            "desc": True,
            "discount": True,
            "skip_trial": False,
            "subscription_preview": True,
            "button_color": "#7047EB",
        },
        "checkout_data": {
            "email": "user@example.com",
            "name": "Sample User",
            "billing_address": [],
            "tax_number": "",
            "discount_code": "",
            "custom": [],
            "variant_quantities": [],
        },
        "expires_at": None,
        "created_at": "2024-10-14T12:36:27.000000Z",
        "updated_at": "2024-10-14T12:36:27.000000Z",
        "test_mode": False,
        "url": "https://my-store.lemonsqueezy.com/checkout/custom/ac470bd4-7c41-474d-b6cd-0f296f5be02a",
    },
    "relationships": {
        "store": {
            "links": {
                "related": "https://api.lemonsqueezy.com/v1/checkouts/ac470bd4-7c41-474d-b6cd-0f296f5be02a/store",
                "self": "https://api.lemonsqueezy.com/v1/checkouts/ac470bd4-7c41-474d-b6cd-0f296f5be02a/relationships/store",
            }
        },
        "variant": {
            "links": {
                "related": "https://api.lemonsqueezy.com/v1/checkouts/ac470bd4-7c41-474d-b6cd-0f296f5be02a/variant",
                "self": "https://api.lemonsqueezy.com/v1/checkouts/ac470bd4-7c41-474d-b6cd-0f296f5be02a/relationships/variant",
            }
        },
    },
    "links": {
        "self": "https://api.lemonsqueezy.com/v1/checkouts/ac470bd4-7c41-474d-b6cd-0f296f5be02a",
    },
}


class MockResponse:
    def __init__(self, payload, status_code=200):
        self._payload = payload
        self.status_code = status_code

    def json(self):
        return self._payload

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(response=self)


def test_get_checkout_returns_model(monkeypatch, client):
    def fake_get(url, headers, timeout):
        return MockResponse({"data": MOCK_CHECKOUT})

    monkeypatch.setattr(checkout_api.requests, "get", fake_get)

    checkout = get_checkout(client, MOCK_CHECKOUT["id"])

    assert isinstance(checkout, Checkout)
    assert checkout.id_ == MOCK_CHECKOUT["id"]


def test_get_checkout_raises_client_error(monkeypatch, client):
    def fake_get(url, headers, timeout):
        return MockResponse({"errors": []}, status_code=404)

    monkeypatch.setattr(checkout_api.requests, "get", fake_get)

    with pytest.raises(LemonSqueezyClientError):
        get_checkout(client, "missing")


def test_list_checkouts_paginates(monkeypatch, client):
    responses = [
        MockResponse({"data": [MOCK_CHECKOUT], "meta": {"page": {"lastPage": 2}}}),
        MockResponse(
            {
                "data": [
                    {
                        **MOCK_CHECKOUT,
                        "id": "second-checkout",
                        "links": {
                            "self": "https://api.lemonsqueezy.com/v1/checkouts/second-checkout"
                        },
                    }
                ],
                "meta": {"page": {"lastPage": 2}},
            }
        ),
    ]

    def fake_get(url, headers, timeout):
        return responses.pop(0)

    monkeypatch.setattr(checkout_api.requests, "get", fake_get)

    checkouts = list_checkouts(client)

    assert len(checkouts) == 2
    assert {checkout.id_ for checkout in checkouts} == {
        MOCK_CHECKOUT["id"],
        "second-checkout",
    }
