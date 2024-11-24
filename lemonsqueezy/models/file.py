"""
A file represents a digital good that can be downloaded by a customer after the product has been purchased.

{
  "type": "files",
  "id": "1",
  "attributes": {
    "variant_id": 168,
    "identifier": "6dce5ba7-76f2-481f-ad1e-9c2bec6eb0e2",
    "name": "my_product.zip",
    "extension": "zip",
    "download_url": "https://app.lemonsqueezy.com/download/6dce5ba7-76f2-481f-ad1e-9c2bec6eb0e2?expires=1636383388&signature=886a63faf7215c54011accfa08578b1b687def66f767092629f263061b3a253a",
    "size": 874694,
    "size_formatted": "854 KB",
    "version": "1.0.0",
    "sort": 1,
    "status": "published",
    "createdAt": "2021-11-05T10:22:14.000000Z",
    "updatedAt": "2021-11-05T16:16:33.000000Z",
    "test_mode": false
  }
}
"""

from typing import Optional

from pydantic import BaseModel, Field

from lemonsqueezy.models import BaseEntity


class _File(BaseEntity):
    """The file object itself"""

    class Attributes(BaseModel):
        """The attributes of a File object"""

        variant_id: int
        identifier: str
        name: str
        extension: str
        download_url: str
        size: int
        size_formatted: str
        version: Optional[str]
        sort: int
        status: str
        createdAt: str
        updatedAt: str
        test_mode: bool

    attributes: Attributes


class File(_File):
    """
    A file represents a digital good that can be downloaded
    by a customer after the product has been purchased.
    """

    class Relationships(BaseModel):
        """The relationships of a File object"""

        class Variant(BaseModel):
            """The Variant that the File belongs to"""

            class Links(BaseModel):
                """The links of the Variant"""

                related: str
                self_: str = Field(..., alias="self")

            links: Links

        variant: Variant

    class Links(BaseModel):
        """The links of a File object"""

        self_: str = Field(..., alias="self")

    relationships: Relationships
    links: Links
