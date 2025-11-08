from lemonsqueezy.api.order import get_order, list_orders
from lemonsqueezy.models.order import Order


def test_get_order(client, order_id):
    order = get_order(client, order_id)
    assert isinstance(order, Order)


def test_list_orders(client):
    orders = list_orders(client)
    assert all(isinstance(order, Order) for order in orders)
