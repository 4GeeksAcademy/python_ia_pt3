from fastapi import HTTPException

from models.shopping_item import DummyMySQL, ShoppingItem, ShoppingItemCreate, database


class ShoppingItemController:
    def __init__(self, repository: DummyMySQL) -> None:
        self.repository = repository

    def list_items(self) -> list[ShoppingItem]:
        return self.repository.select_all()

    def get_item(self, item_id: int) -> ShoppingItem:
        item = self.repository.select_one(item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return item

    def create_item(self, data: ShoppingItemCreate) -> ShoppingItem:
        return self.repository.insert(data)

    def replace_item(self, item_id: int, data: ShoppingItemCreate) -> ShoppingItem:
        item = self.repository.update(item_id, data)
        if item is None:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return item

    def delete_item(self, item_id: int) -> None:
        if not self.repository.delete(item_id):
            raise HTTPException(status_code=404, detail="Producto no encontrado")


controller = ShoppingItemController(database)
