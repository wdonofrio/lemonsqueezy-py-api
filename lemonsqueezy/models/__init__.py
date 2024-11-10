import importlib
import pkgutil

from pydantic import BaseModel, Field


class BaseEntity(BaseModel):
    """The Base Entity Object"""

    type_: str = Field(..., alias="type")
    id_: str = Field(..., alias="id")


__all__ = ["BaseEntity"]

# Dynamically import all modules in the package
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    module = importlib.import_module(f"{__name__}.{module_name}")
    for attr in dir(module):
        if not attr.startswith("_"):
            globals()[attr] = getattr(module, attr)
            __all__.append(attr)
