from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()

DATABASE_URL = "mysql+mysqlconnector://root:dominid@localhost:3306/dimsor"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Rol(Base):
    __tablename__ = "roles"  # Asegúrate que así se llama tu tabla
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    descripcion = Column(String(255))

@app.get("/roles/")
def get_roles():
    db = SessionLocal()
    roles = db.query(Rol).all()
    db.close()
    return [{"id": r.id, "nombre": r.nombre, "descripcion": r.descripcion} for r in roles]