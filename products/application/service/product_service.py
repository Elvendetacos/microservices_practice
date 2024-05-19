from typing import List
from domain.model.product_domain import Product_domain
from domain.repository.product_repository import Product_repository
from domain.use_case.product_use_case import Product_use_case


class Product_service(Product_use_case):
    def __init__(self, product_repository: Product_repository):
        super().__init__(product_repository)

    def add_product(self, product: List[Product_domain]):
        new_product = []
        for product in product:
            new_product.append(self.product_repository.add_product(product))
        return new_product

    def update_product(self, product: List[Product_domain]):
        for product in product:
            og_product = self.product_repository.get_by_id(product.id)
            if og_product is None:
                raise Exception("Product not found")
            og_product.stock = og_product.stock - product.stock
            self.product_repository.update_product(og_product)

    def get_by_id(self, product_id: str) -> Product_domain:
        return self.product_repository.get_by_id(product_id)

    def delete_by_id(self, product_id: str):
        self.product_repository.delete_by_id(product_id)

    def get_all(self) -> List[Product_domain]:
        return self.product_repository.get_all()
