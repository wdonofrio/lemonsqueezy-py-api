import pytest

from lemonsqueezy.api.errors import LemonSqueezyClientError
from lemonsqueezy.api.subscription_items import (
    get_subscription_item,
    list_subscription_items,
)
from lemonsqueezy.models.subscription_item import SubscriptionItem


def test_get_subscription_item(client, subscription_item_id):
    subscription_item = get_subscription_item(client, subscription_item_id)
    assert isinstance(subscription_item, SubscriptionItem)


def test_get_subscription_item_invalid(client):
    with pytest.raises(LemonSqueezyClientError):
        get_subscription_item(client, "999999999")


def test_list_subscription_items(client):
    subscription_items = list_subscription_items(client)
    assert all(
        isinstance(subscription_item, SubscriptionItem)
        for subscription_item in subscription_items
    )
