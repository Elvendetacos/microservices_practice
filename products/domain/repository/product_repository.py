from typing import List
from abc import ABC, abstractmethod

from domain.model.product_domain import Product_domain


class Product_repository(ABC):
    @abstractmethod
    def add_product(self, product: Product_domain):
        raise NotImplemented

    @abstractmethod
    def delete_by_id(self, product_id: str):
        raise NotImplemented

    @abstractmethod
    def get_all(self) -> List[Product_domain]:
        raise NotImplemented
