# API de lista de compras

Mini API construida con FastAPI y organizada con arquitectura MVC. La persistencia se simula mediante `DummyMySQL`: conserva los datos en memoria y representa las consultas parametrizadas que se enviarian a MySQL.

## Arquitectura MVC

```text
.
|-- fast.py
|-- models/
|   `-- shopping_item.py
|-- controllers/
|   `-- shopping_item_controller.py
`-- views/
  `-- shopping_item_view.py
```

- **Modelo:** define los esquemas Pydantic, los datos y las consultas dummy de MySQL.
- **Controlador:** contiene la logica CRUD y decide cuando responder con errores de negocio.
- **Vista:** define la interfaz HTTP con las rutas, codigos de estado y modelos de respuesta.
- **Aplicacion:** `fast.py` configura FastAPI y registra el router de la vista.

## Instalacion

```bash
pipenv install --dev
pipenv shell
```

Tambien puedes instalar las dependencias directamente:

```bash
python -m pip install fastapi uvicorn httpx pytest
```

## Ejecucion

```bash
uvicorn fast:app --reload
```

La API queda disponible en `http://127.0.0.1:8000` y su documentacion interactiva en `http://127.0.0.1:8000/docs`.

## Endpoints

| Metodo | Ruta | Accion |
| --- | --- | --- |
| GET | `/items` | Listar productos |
| GET | `/items/{item_id}` | Consultar un producto |
| POST | `/items` | Crear un producto |
| PUT | `/items/{item_id}` | Reemplazar un producto |
| DELETE | `/items/{item_id}` | Eliminar un producto |

Ejemplo de cuerpo para `POST` y `PUT`:

```json
{
  "name": "Huevos",
  "quantity": 12,
  "purchased": false
}
```

Los campos se validan con Pydantic: `name` debe contener entre 1 y 100 caracteres y `quantity` debe ser al menos 1.

## Pruebas

```bash
python -m pytest test_fast.py -q
```

Los datos son temporales y vuelven a sus valores iniciales cada vez que se reinicia el proceso.
