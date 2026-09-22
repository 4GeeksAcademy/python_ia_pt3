from fastapi import FastAPI

from views.shopping_item_view import router


app = FastAPI(
    title="API de lista de compras",
    description="CRUD con arquitectura MVC y respuestas simuladas de MySQL.",
    version="1.0.0",
)

app.include_router(router)