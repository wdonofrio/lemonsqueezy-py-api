import pytest

from lemonsqueezy.api.errors import LemonSqueezyClientError
from lemonsqueezy.api.store import get_store, list_stores
from lemonsqueezy.models import Store


def test_get_store(store_id):
    store = get_store(store_id)
    assert isinstance(store, Store)


def test_get_store_invalid():
    with pytest.raises(LemonSqueezyClientError) as exc_info:
        get_store("1")

    assert exc_info.value.status_code == 404


def test_list_stores():
    stores = list_stores()
    print(stores)
    assert all(isinstance(store, Store) for store in stores)
