import pytest
import requests

from lemonsqueezy.api import prices as prices_api
from lemonsqueezy.api.errors import LemonSqueezyClientError
from lemonsqueezy.api.prices import get_price, list_prices
from lemonsqueezy.models.prices import Price

MOCK_PRICE = {
    "id": "price-1",
    "type": "prices",
    "attributes": {
        "variant_id": 1,
        "category": "subscription",
        "scheme": "graduated",
        "usage_aggregation": None,
        "unit_price": 999,
        "unit_price_decimal": None,
        "setup_fee_enabled": False,
        "setup_fee": None,
        "package_size": 1,
        "tiers": [],
        "renewal_interval_unit": "month",
        "renewal_interval_quantity": 1,
        "trial_interval_unit": "day",
        "trial_interval_quantity": 14,
        "min_price": None,
        "suggested_price": None,
        "tax_code": "eservice",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z",
    },
    "relationships": {
        "variant": {
            "links": {
                "related": "https://api.lemonsqueezy.test/variants/1",
                "self": "https://api.lemonsqueezy.test/prices/price-1/relationships/variant",
            }
        }
    },
    "links": {
        "self": "https://api.lemonsqueezy.test/prices/price-1",
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


def test_get_price_returns_price_model(monkeypatch, client):
    def fake_get(url, headers, timeout):
        return MockResponse({"data": MOCK_PRICE})

    monkeypatch.setattr(prices_api.requests, "get", fake_get)

    price = get_price(client, "price-1")

    assert isinstance(price, Price)
    assert price.id_ == MOCK_PRICE["id"]


def test_get_price_raises_client_error(monkeypatch, client):
    error_payload = {"errors": [{"status": "404", "title": "Not Found"}]}

    def fake_get(url, headers, timeout):
        return MockResponse(error_payload, status_code=404)

    monkeypatch.setattr(prices_api.requests, "get", fake_get)

    with pytest.raises(LemonSqueezyClientError) as exc_info:
        get_price(client, "missing-price")

    assert exc_info.value.status_code == 404
    assert exc_info.value.response_json == error_payload


def test_list_prices_paginates_until_last_page(monkeypatch, client):
    responses = [
        MockResponse(
            {
                "data": [MOCK_PRICE],
                "meta": {"page": {"lastPage": 2}},
            }
        ),
        MockResponse(
            {
                "data": [
                    {
                        **MOCK_PRICE,
                        "id": "price-2",
                        "links": {
                            "self": "https://api.lemonsqueezy.test/prices/price-2"
                        },
                    }
                ],
                "meta": {"page": {"lastPage": 2}},
            }
        ),
    ]

    def fake_get(url, headers, timeout):
        return responses.pop(0)

    monkeypatch.setattr(prices_api.requests, "get", fake_get)

    prices = list_prices(client)

    assert len(prices) == 2
    assert {price.id_ for price in prices} == {"price-1", "price-2"}
