from lemonsqueezy.api.prices import get_price, list_prices
from lemonsqueezy.models.prices import Price


def test_get_price(client, price_id):
    price = get_price(client, price_id)
    assert isinstance(price, Price)


def test_list_prices(client):
    prices = list_prices(client)
    assert all(isinstance(price, Price) for price in prices)
