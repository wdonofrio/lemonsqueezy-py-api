import os
from typing import Optional

from lemonsqueezy.api.customer import list_customers
from lemonsqueezy.api.file import get_file, list_files
from lemonsqueezy.api.product import get_product, get_product_variants, list_products
from lemonsqueezy.api.store import list_stores
from lemonsqueezy.api.variant import get_variant, list_variants
from lemonsqueezy.models.customer import Customer
from lemonsqueezy.models.file import File
from lemonsqueezy.models.product import Product
from lemonsqueezy.models.store import Store
from lemonsqueezy.models.variant import Variant
from lemonsqueezy.protocols import LemonSqueezyProtocol


class LemonSqueezy(LemonSqueezyProtocol):
    """LemonSqueezy API client"""

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_url: Optional[str] = None,
    ):
        """
        Initialize the LemonSqueezy client.

        Args:
            api_key (Optional[str]): The API key for authentication. Defaults to environment variable LEMONSQUEEZY_API_KEY.
            api_url (Optional[str]): The base URL for the API. Defaults to environment variable LEMONSQUEEZY_API_URL or the official API URL.

        Raises:
            ValueError: If the API key is not provided and not found in the environment variable.
        """
        self.__api_key = api_key or self._get_default_api_key()
        if not self.__api_key:
            raise ValueError(
                "API key is required. Provide it as an argument or set LEMONSQUEEZY_API_KEY in the environment."
            )

        self.__api_url = api_url or self._get_default_api_url()
        if not self.__api_url:
            raise ValueError(
                "API URL is required. Provide it as an argument or set LEMONSQUEEZY_API_URL in the environment."
            )

    @staticmethod
    def _get_default_api_key() -> Optional[str]:
        """Retrieve the default API key from the environment."""
        return os.getenv("LEMONSQUEEZY_API_KEY")

    @staticmethod
    def _get_default_api_url() -> str:
        """Retrieve the default API URL from the environment."""
        return os.getenv("LEMONSQUEEZY_API_URL", "https://api.lemonsqueezy.com/v1")

    @property
    def headers(self) -> dict[str, str]:
        """Get the headers for the request"""
        return {
            "Accept": "application/vnd.api+json",
            "Content-Type": "application/vnd.api+json",
            "Authorization": f"Bearer {self.__api_key}",
        }

    @property
    def base_url(self) -> str:
        """Return the base URL for the API"""
        return self.__api_url

    def list_stores(self) -> list[Store]:
        return list_stores(self)

    def list_customers(self) -> list[Customer]:
        return list_customers(self)

    def get_product(self, product_id: str | int) -> Product:
        return get_product(self, product_id)

    def get_product_variants(self, product_id: str | int) -> list[Product]:
        return get_product_variants(self, product_id)

    def list_products(self) -> list[Product]:
        return list_products(self)

    def get_file(self, file_id: str | int) -> File:
        return get_file(self, file_id)

    def list_files(self) -> list[File]:
        return list_files(self)

    def get_variant(self, variant_id: str | int) -> Product:
        return get_variant(self, variant_id)

    def list_variants(self) -> list[Variant]:
        return list_variants(self)
