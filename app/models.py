from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Creación de la clase Categoria para definir sus atributos en la BD
class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True)
    # El nombre de la categoría debe ser único
    nombre = Column(String(100), unique=True, index=True)
    # Relación 1:M con Producto
    productos = relationship("Producto", back_populates="categorias")
    #back_populates="categoria" va a hacer referencia al atributo categoria dentro de Productos

class Producto(Base):
    __tablename__ = "productos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    precio = Column(Float)
    # Por defecto, el producto tiene stock
    en_stock = Column(Boolean, default=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    categorias = relationship("Categoria", back_populates="productos")

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, index=True)
    email = Column(String(150), unique=True, index=True)
    hashed_password = Column(String(255))