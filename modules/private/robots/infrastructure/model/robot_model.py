# modules/private/robots/infrastructure/model/robot_model.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from modules.database import Base  

class RobotModel(Base):
    __tablename__ = "robots"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    identificador_unico = Column(String(100))
    ip_actual = Column(String(45))
    estado = Column(String(20))
    descripcion = Column(Text)
    fecha_registro = Column(DateTime)