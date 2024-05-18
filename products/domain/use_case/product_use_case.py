from abc import ABC, abstractmethod
from typing import List
from domain.model.product_domain import Product_domain
from domain.repository.product_repository import Product_repository


class Product_use_case(ABC):

    @abstractmethod
    def __init__(self, product_repository: Product_repository):
        self.product_repository = product_repository

    @abstractmethod
    def add_product(self, product: List[Product_domain]):
        raise NotImplemented

    @abstractmethod
    def delete_by_id(self, product_id: str):
        raise NotImplemented

    @abstractmethod
    def get_all(self) -> List[Product_domain]:
        raise NotImplemented
