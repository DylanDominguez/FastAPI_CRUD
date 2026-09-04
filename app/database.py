from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#url que define la conexion a la base de datos
DATABASE_URL = "mysql+pymysql://root:admin@localhost:3306/fastapi_crud"

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)