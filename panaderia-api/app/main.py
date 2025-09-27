from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, get_db, create_tables
from .api.v1.productos import router as productos_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Panadería",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(productos_router)

@app.on_event("startup")
async def startup():
    create_tables()

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de Panadería"}

@app.post("/api/v1/productos/", response_model=schemas.Producto)
def create_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    db_producto = crud.get_producto_by_sku(db, sku=producto.sku)
    if db_producto:
        raise HTTPException(status_code=400, detail="SKU ya existe")
    return crud.create_producto(db=db, producto=producto)

@app.get("/api/v1/productos/", response_model=list[schemas.Producto])
def read_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    productos = crud.get_productos(db, skip=skip, limit=limit)
    return productos

@app.get("/api/v1/productos/{producto_id}", response_model=schemas.Producto)
def read_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = crud.get_producto(db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@app.put("/api/v1/productos/{producto_id}", response_model=schemas.Producto)
def update_producto(producto_id: int, producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    db_producto = crud.update_producto(db, producto_id, producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@app.delete("/api/v1/productos/{producto_id}")
def delete_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = crud.delete_producto(db, producto_id)
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
