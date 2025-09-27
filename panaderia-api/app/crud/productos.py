from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from .. import models, schemas
from fastapi import HTTPException, status

def crear_producto(db: Session, producto_in: schemas.ProductoCreate):
    try:
        db_producto = models.Producto(**producto_in.dict())
        db.add(db_producto)
        db.commit()
        db.refresh(db_producto)
        return db_producto
    except IntegrityError:
        db.rollback()
        raise ValueError("SKU duplicado")

def listar_productos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Producto).offset(skip).limit(limit).all()

def obtener_producto(db: Session, id: int):
    return db.query(models.Producto).filter(models.Producto.id == id).first()

def actualizar_producto(db: Session, id: int, datos: schemas.ProductoUpdate):
    try:
        producto = db.query(models.Producto).filter(models.Producto.id == id)
        if not producto.first():
            return None
        producto.update(datos.dict(exclude_unset=True))
        db.commit()
        return producto.first()
    except IntegrityError:
        db.rollback()
        raise ValueError("SKU duplicado")

def eliminar_producto(db: Session, id: int) -> bool:
    producto = db.query(models.Producto).filter(models.Producto.id == id).first()
    if producto:
        db.delete(producto)
        db.commit()
        return True
    return False
