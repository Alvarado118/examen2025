from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas

def crear_producto(db: Session, producto_in: schemas.ProductoCreate):
    producto = models.Producto(**producto_in.dict())
    db.add(producto)
    try:
        db.commit()
        db.refresh(producto)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="SKU ya existe")
    return producto

def listar_productos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Producto).order_by(models.Producto.id).offset(skip).limit(limit).all()

def obtener_producto(db: Session, id: int):
    producto = db.get(models.Producto, id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

def actualizar_producto(db: Session, id: int, datos: schemas.ProductoUpdate):
    producto = obtener_producto(db, id)
    for k, v in datos.dict(exclude_unset=True).items():
        setattr(producto, k, v)
    try:
        db.commit()
        db.refresh(producto)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="SKU ya existe")
    return producto

def eliminar_producto(db: Session, id: int):
    producto = obtener_producto(db, id)
    db.delete(producto)
    db.commit()
    return True

def get_producto_by_sku(db: Session, sku: str):
    return db.query(models.Producto).filter(models.Producto.sku == sku).first()
