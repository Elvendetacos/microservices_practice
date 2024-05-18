from fastapi import APIRouter
from typing import List
from infraestructure.repository import product_repository_impl
from application.service.product_service import Product_service
from domain.model.product_domain import Product_domain
from infraestructure.schema.Product_entity import Product_entity
from infraestructure.web.dto.response.base_response import Base_response
from infraestructure.mappers.product_mapper import map_list_entity_to_domain

controller = APIRouter()
repository = product_repository_impl.Product_repository_imp()
service = Product_service(repository)


@controller.get("/")
def get_products():
    products = service.get_all()
    return products


@controller.post("/create", response_model=Base_response)
def create_products(product: List[Product_entity]):
    product = map_list_entity_to_domain(product)
    product_save = service.add_product(product)
    return Base_response(data=product_save, message="Product created successfully")


@controller.delete("/delete/{product_id}", response_model=Base_response)
def delete_product(product_id: str):
    service.delete_by_id(product_id)
    return Base_response(data=None, message="Product deleted successfully")



