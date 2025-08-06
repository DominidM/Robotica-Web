from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from modules.database import Base

class UsuarioModel(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    registro_key = Column(String, nullable=False)
    rol_id = Column(Integer, ForeignKey("roles.id"), nullable=False) 
    email = Column(String, nullable=True)
    password_hash = Column(String, nullable=True)
    fecha_registro = Column(DateTime, nullable=True)