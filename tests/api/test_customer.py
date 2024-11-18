import pytest

from lemonsqueezy.api.customer import (
    create_customer,
    get_customer,
    list_customers,
    update_customer,
)
from lemonsqueezy.api.errors import LemonSqueezyClientError
from lemonsqueezy.models.customer import (
    Customer,
    CustomerCreate,
    CustomerList,
    CustomerPatch,
)


@pytest.fixture
def customer_create(store_id):
    return CustomerCreate(
        data=CustomerCreate.Data(
            type="customers",
            attributes=CustomerCreate.Data.Attributes(
                name="John Doe",
                email="johndoe@example.com",
                city="New York",
                region="NY",
                country="US",
            ),
            relationships=CustomerCreate.Data.Relationships(
                store=CustomerCreate.Data.Relationships.Store(
                    data=CustomerCreate.Data.Relationships.Store.StoreData(
                        type="stores", id=store_id
                    )
                )
            ),
        )
    )


@pytest.fixture
def customer_patch(customer_id):
    return CustomerPatch(
        data=CustomerPatch.Data(
            type="customers",
            id=customer_id,
            attributes=CustomerPatch.Data.Attributes(
                name="John Doe", email="johndoe@example.com", status="archived"
            ),
        )
    )


def test_create_customer(customer_create):
    with pytest.raises(LemonSqueezyClientError) as exc_info:
        create_customer(customer_create)

    assert exc_info.value.status_code == 422  # Customer already exists


def test_get_customer(customer_id):
    customer = get_customer(customer_id)
    assert isinstance(customer, Customer)


def test_get_customer_invalid():
    with pytest.raises(LemonSqueezyClientError) as exc_info:
        get_customer("1")

    assert exc_info.value.status_code == 404


def test_update_customer(customer_patch):
    customer = update_customer(customer_patch)
    assert isinstance(customer, Customer)


def test_list_customers():
    customers = list_customers()
    assert all(isinstance(customer, CustomerList) for customer in customers)
