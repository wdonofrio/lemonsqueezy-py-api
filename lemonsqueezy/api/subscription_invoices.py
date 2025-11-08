import requests

from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.subscription_invoice import SubscriptionInvoice
from lemonsqueezy.protocols import LemonSqueezyProtocol


@handle_http_errors
def get_subscription_invoice(
    client: LemonSqueezyProtocol, subscription_invoice_id: str | int
) -> SubscriptionInvoice:
    """Retrieve a subscription invoice by ID."""
    response = requests.get(
        f"{client.base_url}/subscription-invoices/{subscription_invoice_id}",
        headers=client.headers,
        timeout=30,
    )
    response.raise_for_status()
    invoice_data = response.json().get("data", {})
    return SubscriptionInvoice(**invoice_data)


@handle_http_errors
def list_subscription_invoices(
    client: LemonSqueezyProtocol, page: int = 1, per_page: int = 10
) -> list[SubscriptionInvoice]:
    """List subscription invoices, exhausting pagination."""
    invoices: list[SubscriptionInvoice] = []
    while True:
        response = requests.get(
            f"{client.base_url}/subscription-invoices?page[number]={page}&page[size]={per_page}",
            headers=client.headers,
            timeout=30,
        )
        response.raise_for_status()
        response_data = response.json()
        invoices.extend(
            SubscriptionInvoice(**invoice_data)
            for invoice_data in response_data.get("data", [])
        )

        meta = response_data.get("meta", {}).get("page", {})
        if page >= meta.get("lastPage", 1):
            break
        page += 1

    return invoices
