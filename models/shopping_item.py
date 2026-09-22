from typing import Annotated

from pydantic import BaseModel, Field


class ShoppingItemCreate(BaseModel):
    name: Annotated[str, Field(min_length=1, max_length=100)]
    quantity: Annotated[int, Field(ge=1)] = 1
    purchased: bool = False


class ShoppingItem(ShoppingItemCreate):
    id: int


class DummyMySQL:
    """Simula las respuestas de las consultas que se enviarian a MySQL."""

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._items: dict[int, ShoppingItem] = {
            1: ShoppingItem(id=1, name="Leche", quantity=2, purchased=False),
            2: ShoppingItem(id=2, name="Pan", quantity=1, purchased=True),
        }
        self._next_id = 3

    def select_all(self) -> list[ShoppingItem]:
        query = "SELECT id, name, quantity, purchased FROM shopping_items"
        _dummy_query_response = {"query": query, "rowcount": len(self._items)}
        return list(self._items.values())

    def select_one(self, item_id: int) -> ShoppingItem | None:
        query = "SELECT id, name, quantity, purchased FROM shopping_items WHERE id = %s"
        _dummy_query_response = {
            "query": query,
            "params": (item_id,),
            "rowcount": int(item_id in self._items),
        }
        return self._items.get(item_id)

    def insert(self, data: ShoppingItemCreate) -> ShoppingItem:
        query = (
            "INSERT INTO shopping_items (name, quantity, purchased) "
            "VALUES (%s, %s, %s)"
        )
        item = ShoppingItem(id=self._next_id, **data.model_dump())
        self._items[item.id] = item
        self._next_id += 1
        _dummy_query_response = {
            "query": query,
            "params": (data.name, data.quantity, data.purchased),
            "lastrowid": item.id,
            "rowcount": 1,
        }
        return item

    def update(self, item_id: int, data: ShoppingItemCreate) -> ShoppingItem | None:
        if item_id not in self._items:
            return None

        query = (
            "UPDATE shopping_items SET name = %s, quantity = %s, purchased = %s "
            "WHERE id = %s"
        )
        item = ShoppingItem(id=item_id, **data.model_dump())
        self._items[item_id] = item
        _dummy_query_response = {
            "query": query,
            "params": (data.name, data.quantity, data.purchased, item_id),
            "rowcount": 1,
        }
        return item

    def delete(self, item_id: int) -> bool:
        query = "DELETE FROM shopping_items WHERE id = %s"
        deleted = self._items.pop(item_id, None) is not None
        _dummy_query_response = {
            "query": query,
            "params": (item_id,),
            "rowcount": int(deleted),
        }
        return deleted


database = DummyMySQL()
