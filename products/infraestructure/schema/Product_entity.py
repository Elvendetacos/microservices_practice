from pydantic import BaseModel


class Product_entity(BaseModel):
    name: str
    price: int
    stock: int
