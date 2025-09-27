from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

CATEGORIAS_VALIDAS = {"Pan", "Pasteleria", "Bebidas", "Otros"}

class ProductoBase(BaseModel):
    nombre: str = Field(..., max_length=150)
    sku: str = Field(..., max_length=20)
    categoria: str
    precio_unitario: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    disponible: Optional[bool] = True

    @validator("categoria")
    def categoria_valida(cls, v):
        if v not in CATEGORIAS_VALIDAS:
            raise ValueError("Categoría inválida")
        return v

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = Field(None, max_length=150)
    categoria: Optional[str]
    precio_unitario: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    disponible: Optional[bool]

    @validator("categoria")
    def categoria_valida(cls, v):
        if v and v not in CATEGORIAS_VALIDAS:
            raise ValueError("Categoría inválida")
        return v

class Producto(ProductoBase):
    id: int
    fecha_registro: datetime
    fecha_actualizacion: datetime

    class Config:
        orm_mode = True

class ProductoOut(ProductoBase):
    id: int
    fecha_registro: datetime
    fecha_actualizacion: Optional[datetime]

    class Config:
        orm_mode = True
