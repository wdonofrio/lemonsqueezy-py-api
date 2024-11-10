from lemonsqueezy.api.user import get_user
from lemonsqueezy.models import User


def test_get_user():
    user = get_user()
    assert isinstance(user, User)
