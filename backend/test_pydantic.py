# from pydantic import validate_call

# @validate_call
# def calculate_total(price: int, quantity: int) -> int:
#     return price * quantity

# print(calculate_total("ten",5))  

from pydantic import BaseModel

class Product(BaseModel):
    product_name: str
    price: float
    in_stock: bool=True

product = Product(product_name="Laptop", price=1500,in_stock=False)
print(product.model_dump_json()) 