from sqlalchemy import Column, Integer, String
from modules.database import Base

class RolModel(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(255))