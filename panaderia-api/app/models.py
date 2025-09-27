from sqlalchemy import Column, Integer, String, Numeric, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    sku = Column(String(20), unique=True, nullable=False, index=True)
    categoria = Column(String(20), nullable=False)
    precio_unitario = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, nullable=False, default=20)
    disponible = Column(Boolean, default=True)
    fecha_registro = Column(DateTime(timezone=True), server_default=func.now())
    fecha_actualizacion = Column(DateTime(timezone=True), onupdate=func.now())
    nombre = Column(String(150), nullable=False)
    sku = Column(String, unique=True, nullable=False)
    categoria = Column(Enum(CategoriaEnum), nullable=False)
    precio_unitario = Column(Float(precision=2), nullable=False)
    stock = Column(Integer, default=20)
    disponible = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
