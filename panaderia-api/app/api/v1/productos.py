from fastapi import APIRouter, Depends, status, HTTPException, Query
from typing import List
from sqlalchemy.orm import Session
from ... import crud, schemas
from ...deps import get_db

router = APIRouter(prefix="/api/v1/productos", tags=["productos"])

@router.post("/", response_model=schemas.ProductoOut, status_code=status.HTTP_201_CREATED)
def crear_producto(producto_in: schemas.ProductoCreate, db: Session = Depends(get_db)):
    try:
        producto = crud.crear_producto(db, producto_in)
        return producto
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/", response_model=List[schemas.ProductoOut])
def listar_productos(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, le=100),
    db: Session = Depends(get_db)
):
    return crud.listar_productos(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=schemas.ProductoOut)
def obtener_producto(id: int, db: Session = Depends(get_db)):
    producto = crud.obtener_producto(db, id)
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto con id {id} no encontrado"
        )
    return producto

@router.put("/{id}", response_model=schemas.ProductoOut)
def actualizar_producto(id: int, datos: schemas.ProductoUpdate, db: Session = Depends(get_db)):
    try:
        producto = crud.actualizar_producto(db, id, datos)
        if not producto:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Producto con id {id} no encontrado"
            )
        return producto
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_producto(id: int, db: Session = Depends(get_db)):
    if not crud.eliminar_producto(db, id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Producto con id {id} no encontrado"
        )
    return None
