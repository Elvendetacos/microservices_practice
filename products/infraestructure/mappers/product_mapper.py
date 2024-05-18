from domain.model.product_domain import Product_domain
from infraestructure.schema.models_factory import Product


def to_domain_product(db_product: Product) -> Product_domain:
    return Product_domain(
        name=db_product.name,
        price=db_product.price,
        stock=db_product.stock
    )


def map_entity_to_domain(product_entity):
    return Product_domain(
        name=product_entity.name,
        price=product_entity.price,
        stock=product_entity.stock
    )


def map_list_entity_to_domain(products_entity):
    return [map_entity_to_domain(product) for product in products_entity]


def to_db_product(domain_product: Product_domain) -> Product:
    return Product(
        id=domain_product.get_id(),
        name=domain_product.get_name(),
        price=domain_product.get_price(),
        stock=domain_product.get_stock()
    )


def to_dict(domain_product: Product_domain) -> dict:
    return {
        "id": domain_product.get_id(),
        "name": domain_product.get_name(),
        "price": domain_product.get_price(),
        "stock": domain_product.get_stock()
    }
