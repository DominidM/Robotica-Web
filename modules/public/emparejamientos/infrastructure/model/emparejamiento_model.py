from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from modules.database import Base

class EmparejamientoModel(Base):
    __tablename__ = "emparejamientos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    robot_id = Column(Integer, ForeignKey("robots.id"), nullable=False)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime, nullable=True)
    estado = Column(String(50), nullable=True)

    usuario = relationship("UsuarioModel", backref="emparejamientos")
    robot = relationship("RobotModel", backref="emparejamientos")