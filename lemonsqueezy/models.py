from typing import Dict

from pydantic import BaseModel, Field


class Attributes(BaseModel):
    """The Attributes Object in the User Object"""

    name: str
    email: str
    color: str
    avatar_url: str
    has_custom_avatar: bool
    createdAt: str
    updatedAt: str


class User(BaseModel):
    """The User Object
    https://docs.lemonsqueezy.com/api/users/the-user-object

    Example:
    {
    "meta": {
        "test_mode": true
    },
    "jsonapi": {
        "version": "1.0"
    },
    "links": {
        "self": "https://api.lemonsqueezy.com/v1/users/1"
    },
    "data": {
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
        },
        "links": {
        "self": "https://api.lemonsqueezy.com/v1/users/1"
        }
    }
    }

    """

    type_: str = Field(..., alias="type")
    id_: str = Field(..., alias="id")
    attributes: Attributes
    links: Dict
