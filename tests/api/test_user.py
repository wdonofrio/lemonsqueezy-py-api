from lemonsqueezy.api.user import get_user
from lemonsqueezy.models.user import User


def test_get_user(client) -> None:
    user = get_user(client)
    assert isinstance(user, User)
