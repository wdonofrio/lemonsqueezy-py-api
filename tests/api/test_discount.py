import pytest
import requests

from lemonsqueezy.api import discount as discount_api
from lemonsqueezy.api.discount import get_discount, list_discounts
from lemonsqueezy.api.errors import LemonSqueezyClientError
from lemonsqueezy.models.discount import Discount

MOCK_DISCOUNT = {
    "type": "discounts",
    "id": "1",
    "attributes": {
        "store_id": 1,
        "name": "10%",
        "code": "10PERC",
        "amount": 10,
        "amount_type": "percent",
        "is_limited_to_products": False,
        "is_limited_redemptions": False,
        "max_redemptions": 0,
        "starts_at": None,
        "expires_at": None,
        "duration": "once",
        "duration_in_months": 1,
        "status": "published",
        "status_formatted": "Published",
        "created_at": "2021-05-24T14:15:06.000000Z",
        "updated_at": "2021-05-24T14:15:06.000000Z",
        "test_mode": False,
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


def test_get_discount_returns_model(monkeypatch, client):
    def fake_get(url, headers, timeout):
        return MockResponse({"data": MOCK_DISCOUNT})

    monkeypatch.setattr(discount_api.requests, "get", fake_get)

    discount = get_discount(client, MOCK_DISCOUNT["id"])

    assert isinstance(discount, Discount)
    assert discount.id_ == MOCK_DISCOUNT["id"]


def test_get_discount_raises_client_error(monkeypatch, client):
    def fake_get(url, headers, timeout):
        return MockResponse({"errors": []}, status_code=422)

    monkeypatch.setattr(discount_api.requests, "get", fake_get)

    with pytest.raises(LemonSqueezyClientError):
        get_discount(client, "missing")


def test_list_discounts_paginates(monkeypatch, client):
    responses = [
        MockResponse({"data": [MOCK_DISCOUNT], "meta": {"page": {"lastPage": 2}}}),
        MockResponse(
            {
                "data": [
                    {
                        **MOCK_DISCOUNT,
                        "id": "2",
                        "attributes": {
                            **MOCK_DISCOUNT["attributes"],
                            "name": "20%",
                            "code": "20PERC",
                        },
                    }
                ],
                "meta": {"page": {"lastPage": 2}},
            }
        ),
    ]

    def fake_get(url, headers, timeout):
        return responses.pop(0)

    monkeypatch.setattr(discount_api.requests, "get", fake_get)

    discounts = list_discounts(client)

    assert len(discounts) == 2
    assert {discount.id_ for discount in discounts} == {"1", "2"}
