from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import Depends
from database import SessionmLocal

#url que define la conexion a la base de datos
DATABASE_URL = "mysql+pymysql://root:admin@localhost:3306/ecommerce_db"

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def obtener_db():
    db = SessionmLocal()
    try:
        yield db
    finally:
        db.close()