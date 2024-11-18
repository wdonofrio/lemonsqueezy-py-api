import requests

from lemonsqueezy.api import BASE_URL, get_headers
from lemonsqueezy.api.errors import handle_http_errors
from lemonsqueezy.models.customer import (
    Customer,
    CustomerCreate,
    CustomerList,
    CustomerPatch,
)


@handle_http_errors
def create_customer(customer_data: CustomerCreate) -> Customer:
    """Create a customer"""
    response = requests.post(
        f"{BASE_URL}/customers",
        headers=get_headers(),
        json=customer_data.model_dump(by_alias=True),
        timeout=30,
    )
    response.raise_for_status()
    response_data = response.json().get("data", {})
    return Customer(**response_data)


@handle_http_errors
def get_customer(customer_id: str | int) -> Customer:
    """Get a customer"""
    response = requests.get(
        f"{BASE_URL}/customers/{customer_id}", headers=get_headers(), timeout=30
    )
    response.raise_for_status()
    customer_data = response.json().get("data", {})
    return Customer(**customer_data)


@handle_http_errors
def update_customer(customer_data: CustomerPatch) -> Customer:
    """Update a customer"""
    if (customer_id := customer_data.data.model_dump(by_alias=True).get("id")) is None:
        raise ValueError("Customer ID is required in CustomerPatch data.")

    response = requests.patch(
        f"{BASE_URL}/customers/{customer_id}",
        headers=get_headers(),
        json=customer_data.model_dump(by_alias=True),
        timeout=30,
    )
    response.raise_for_status()
    response_data = response.json().get("data", {})
    return Customer(**response_data)


@handle_http_errors
def list_customers(page: int = 1, per_page: int = 10) -> list[CustomerList]:
    """List the customers with pagination"""
    customers = []
    while True:
        response = requests.get(
            f"{BASE_URL}/customers?page[number]={page}&page[size]={per_page}",
            headers=get_headers(),
            timeout=30,
        )
        response.raise_for_status()
        response_data = response.json()

        customers_data = response_data.get("data", [])
        for customer_data in customers_data:
            # TODO: Investigate why this translation was needed and alias didn't work
            if "license-keys" in customer_data["relationships"]:
                customer_data["relationships"]["license_keys"] = customer_data[
                    "relationships"
                ].pop("license-keys")
            customers.append(CustomerList(**customer_data))

        meta = response_data.get("meta", {}).get("page", {})
        if page >= meta.get("lastPage", 1):
            break
        page += 1

    return customers
