from pydantic import BaseModel, Field


class BaseEntity(BaseModel):
    """The Base Entity Object"""

    type_: str = Field(..., alias="type")
    id_: str = Field(..., alias="id")


__all__ = ["BaseEntity"]
