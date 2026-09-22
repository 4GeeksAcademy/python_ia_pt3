from fastapi import APIRouter, Response, status

from controllers.shopping_item_controller import controller
from models.shopping_item import ShoppingItem, ShoppingItemCreate


router = APIRouter()


@router.get("/", tags=["Estado"])
def read_root() -> dict[str, str]:
    return {"message": "API de lista de compras disponible"}


@router.get("/items", response_model=list[ShoppingItem], tags=["Compras"])
def list_items() -> list[ShoppingItem]:
    return controller.list_items()


@router.get("/items/{item_id}", response_model=ShoppingItem, tags=["Compras"])
def get_item(item_id: int) -> ShoppingItem:
    return controller.get_item(item_id)


@router.post(
    "/items",
    response_model=ShoppingItem,
    status_code=status.HTTP_201_CREATED,
    tags=["Compras"],
)
def create_item(data: ShoppingItemCreate) -> ShoppingItem:
    return controller.create_item(data)


@router.put("/items/{item_id}", response_model=ShoppingItem, tags=["Compras"])
def replace_item(item_id: int, data: ShoppingItemCreate) -> ShoppingItem:
    return controller.replace_item(item_id, data)


@router.delete(
    "/items/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Compras"],
)
def delete_item(item_id: int) -> Response:
    controller.delete_item(item_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
