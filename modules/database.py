from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cambia el driver a "mysql+mysqlclient" o "mysql+pymysql" según lo que tengas instalado
SQLALCHEMY_DATABASE_URL = "mysql+mysqlclient://root:dominid@localhost:3306/dimsor"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()