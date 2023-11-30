from fastapi import APIRouter
from model import Product,ProductIn
from db import products, database

router = APIRouter()


@router.get("/products/", response_model=list[Product])
async def get_products():
    query = products.select()
    return await database.fetch_all(query)


@router.get("/products/{product_id}", response_model=Product | None)
async def one_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database.fetch_one(query)


@router.post("/products/", response_model=str)
async def creat_product(product: ProductIn):
    query = products.insert().values(
        title=product.title,
        description=product.description,
        price=product.price,
    )
    await database.execute(query)
    return f"Товар добавлен"


@router.put("/products/{product_id}")
async def edit_product(product_id: int, new_product: ProductIn):
    query = (
        products.update()
        .where(products.c.id == product_id)
        .values(
            title=new_product.title,
            description=new_product.description,
            price=new_product.price,
        )
    )
    await database.execute(query)
    return f"Пользователь изменен"


@router.delete("/products/{product_id}")
async def del_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return f"Пользователь удален"