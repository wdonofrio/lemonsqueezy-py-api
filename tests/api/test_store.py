import pytest

from lemonsqueezy.api.errors import LemonSqueezyClientError
from lemonsqueezy.api.store import get_store, list_stores
from lemonsqueezy.models.store import Store


def test_get_store(client, store_id) -> None:
    store = get_store(client, store_id)
    assert isinstance(store, Store)


def test_get_store_invalid(client) -> None:
    with pytest.raises(LemonSqueezyClientError) as exc_info:
        get_store(client, "1")

    assert exc_info.value.status_code == 404


def test_list_stores(client) -> None:
    stores = list_stores(client)
    print(stores)
    assert all(isinstance(store, Store) for store in stores)
