from abc import ABC
from typing import List

from infraestructure.configuration.db import SessionLocal
from infraestructure.schema.models_factory import Product
from domain.repository.product_repository import Product_repository
from infraestructure.mappers.product_mapper import to_db_product, to_dict
from domain.model.product_domain import Product_domain as DomainProduct


class Product_repository_imp(Product_repository, ABC):
    def __init__(self):
        self.db = SessionLocal()

    def add_product(self, product: DomainProduct):
        db_product = to_db_product(product)
        print(db_product)
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        self.db.close()
        return to_dict(product)

    def delete_by_id(self, product_id: str):
        self.db.query(Product).filter(Product.id == product_id).delete()
        self.db.commit()
        self.db.close()

    def get_all(self) -> List[Product]:
        return self.db.query(Product).all()
