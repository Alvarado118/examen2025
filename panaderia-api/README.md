# Sistema de Gestión de Productos de Panadería

API REST construida con FastAPI para gestionar productos de panadería.

## Instalación

```bash
# Clonar repositorio
git clone <url-repositorio>

# Instalar dependencias
python -m pip install -r requirements.txt

# Iniciar servidor
python -m uvicorn app.main:app --reload
```

## Endpoints

- POST /api/v1/productos/ - Crear producto
- GET /api/v1/productos/ - Listar productos
- GET /api/v1/productos/{id} - Obtener producto
- PUT /api/v1/productos/{id} - Actualizar producto
- DELETE /api/v1/productos/{id} - Eliminar producto

## Documentación

Accede a la documentación en: http://localhost:8000/docs
