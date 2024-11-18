from lemonsqueezy.api.user import get_user
from lemonsqueezy.models.user import User


def test_get_user() -> None:
    user = get_user()
    assert isinstance(user, User)
