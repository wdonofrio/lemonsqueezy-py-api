import pytest
import requests

from lemonsqueezy.api import discount_redemption as redemptions_api
from lemonsqueezy.api.discount_redemption import (
    get_discount_redemption,
    list_discount_redemptions,
)
from lemonsqueezy.api.errors import LemonSqueezyClientError
from lemonsqueezy.models.discount_redemption import DiscountRedemption

MOCK_REDEMPTION = {
    "type": "discount-redemptions",
    "id": "1",
    "attributes": {
        "discount_id": 1,
        "order_id": 1,
        "discount_name": "10%",
        "discount_code": "10PERC",
        "discount_amount": 10,
        "discount_amount_type": "percent",
        "amount": 999,
        "created_at": "2024-02-07T10:30:01.000000Z",
        "updated_at": "2024-02-07T10:30:01.000000Z",
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


def test_get_discount_redemption_returns_model(monkeypatch, client):
    def fake_get(url, headers, timeout):
        return MockResponse({"data": MOCK_REDEMPTION})

    monkeypatch.setattr(redemptions_api.requests, "get", fake_get)

    redemption = get_discount_redemption(client, MOCK_REDEMPTION["id"])

    assert isinstance(redemption, DiscountRedemption)
    assert redemption.id_ == MOCK_REDEMPTION["id"]


def test_get_discount_redemption_raises_client_error(monkeypatch, client):
    def fake_get(url, headers, timeout):
        return MockResponse({"errors": []}, status_code=400)

    monkeypatch.setattr(redemptions_api.requests, "get", fake_get)

    with pytest.raises(LemonSqueezyClientError):
        get_discount_redemption(client, "missing")


def test_list_discount_redemptions_paginates(monkeypatch, client):
    responses = [
        MockResponse({"data": [MOCK_REDEMPTION], "meta": {"page": {"lastPage": 2}}}),
        MockResponse(
            {
                "data": [
                    {
                        **MOCK_REDEMPTION,
                        "id": "2",
                        "attributes": {
                            **MOCK_REDEMPTION["attributes"],
                            "order_id": 2,
                        },
                    }
                ],
                "meta": {"page": {"lastPage": 2}},
            }
        ),
    ]

    def fake_get(url, headers, timeout):
        return responses.pop(0)

    monkeypatch.setattr(redemptions_api.requests, "get", fake_get)

    redemptions = list_discount_redemptions(client)

    assert len(redemptions) == 2
    assert {redemption.id_ for redemption in redemptions} == {"1", "2"}
