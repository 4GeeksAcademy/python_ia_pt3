from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="API de Contactos",
    version="1.0.0",
    description="API monolítica para gestionar contactos usando memoria local."
)


class Contact(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    tlf: str = Field(..., min_length=5, max_length=20)


contacts = [
    {"id": 1, "name": "Juan", "tlf": "123456789"},
    {"id": 2, "name": "Ana", "tlf": "987654321"},
]


@app.get("/contacts")
def get_contacts():
    return contacts


@app.get("/contacts/{contact_id}")
def get_contact(contact_id: int):
    for contact in contacts:
        if contact["id"] == contact_id:
            return contact

    raise HTTPException(status_code=404, detail="Contacto no encontrado")


@app.post("/contacts", status_code=status.HTTP_201_CREATED)
def create_contact(contact: Contact):
    next_id = max((item["id"] for item in contacts), default=0) + 1
    new_contact = {
        "id": next_id,
        "name": contact.name,
        "tlf": contact.tlf,
    }
    contacts.append(new_contact)
    return new_contact


@app.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact: Contact):
    for index, item in enumerate(contacts):
        if item["id"] == contact_id:
            contacts[index]["name"] = contact.name
            contacts[index]["tlf"] = contact.tlf
            return contacts[index]

    raise HTTPException(status_code=404, detail="Contacto no encontrado")


@app.delete("/contacts/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contact(contact_id: int):
    for index, item in enumerate(contacts):
        if item["id"] == contact_id:
            contacts.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail="Contacto no encontrado")







if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

