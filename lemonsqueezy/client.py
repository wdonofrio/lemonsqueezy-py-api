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


class LemonSqueezy:
    def __init__(self, api_key: str, api_url: str = "https://api.lemonsqueezy.com/v1"):
        self.api_key = api_key
        self.api_url = api_url

    def list_stores(self) -> list[Store]:
        return list_stores()

    def list_customers(self) -> list[Customer]:
        return list_customers()

    def get_product(self, product_id: str | int) -> Product:
        return get_product(product_id)

    def get_product_variants(self, product_id: str | int) -> list[Product]:
        return get_product_variants(product_id)

    def list_products(self) -> list[Product]:
        return list_products()

    def get_file(self, file_id: str | int) -> File:
        return get_file(file_id)

    def list_files(self) -> list[File]:
        return list_files()

    def get_variant(self, variant_id: str | int) -> Product:
        return get_variant(variant_id)

    def list_variants(self) -> list[Variant]:
        return list_variants()
