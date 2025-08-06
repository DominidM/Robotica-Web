from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RobotModel(Base):
    __tablename__ = "robots"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    identificador_unico = Column(String(100))
    ip_actual = Column(String(45))
    estado = Column(String(20))
    descripcion = Column(Text)
    fecha_registro = Column(DateTime)