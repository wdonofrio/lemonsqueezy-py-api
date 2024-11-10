"""The User Object: https://docs.lemonsqueezy.com/api/users/the-user-object
A user represents your personal user account that you use to log into Lemon Squeezy.

{
  "type": "users",
  "id": "1",
  "attributes": {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "color": "#898FA9",
    "avatar_url": "https://www.gravatar.com/avatar/1ace5b3965c59dbcd1db79d85da75048?d=blank",
    "has_custom_avatar": false,
    "createdAt": "2024-05-24T14:08:31.000000Z",
    "updatedAt": "2024-08-26T13:24:54.000000Z"
  }
}

"""

from pydantic import BaseModel

from lemonsqueezy.models import BaseEntity


class User(BaseEntity):
    """The User Object"""

    class Attributes(BaseModel):
        """The Attributes sub-object in the User Object"""

        name: str
        email: str
        color: str
        avatar_url: str
        has_custom_avatar: bool
        createdAt: str
        updatedAt: str

    attributes: Attributes
