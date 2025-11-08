import pytest

from lemonsqueezy.api.errors import LemonSqueezyClientError
from lemonsqueezy.api.subscription_invoices import (
    get_subscription_invoice,
    list_subscription_invoices,
)
from lemonsqueezy.models.subscription_invoice import SubscriptionInvoice


def test_get_subscription_invoice(client, subscription_invoice_id):
    subscription_invoice = get_subscription_invoice(client, subscription_invoice_id)
    assert isinstance(subscription_invoice, SubscriptionInvoice)


def test_get_subscription_invoice_invalid(client):
    with pytest.raises(LemonSqueezyClientError):
        get_subscription_invoice(client, "999999999")


def test_list_subscription_invoices(client):
    subscription_invoices = list_subscription_invoices(client)
    assert all(
        isinstance(subscription_invoice, SubscriptionInvoice)
        for subscription_invoice in subscription_invoices
    )
