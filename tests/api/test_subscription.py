import pytest

from lemonsqueezy.api.errors import LemonSqueezyClientError
from lemonsqueezy.api.subscription import get_subscription, list_subscriptions
from lemonsqueezy.models.subscription import Subscription


def test_get_subscription(client, subscription_id):
    subscription = get_subscription(client, subscription_id)
    assert isinstance(subscription, Subscription)


def test_get_subscription_invalid(client):
    with pytest.raises(LemonSqueezyClientError):
        get_subscription(client, "999999999")


def test_list_subscriptions(client):
    subscriptions = list_subscriptions(client)
    assert all(isinstance(subscription, Subscription) for subscription in subscriptions)
