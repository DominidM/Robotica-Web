from sqlalchemy import Column, Integer, ForeignKey, Enum, Text, DateTime
from sqlalchemy.orm import relationship
from modules.database import Base
from modules.public.sesiones.infrastructure.model.sesiones_model import SesionModel
import enum

class RemitenteEnum(enum.Enum):
    usuario = "usuario"
    robot = "robot"

class MensajeModel(Base):
    __tablename__ = "mensajes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sesion_id = Column(Integer, ForeignKey("sesiones.id"), nullable=False)
    remitente = Column(Enum(RemitenteEnum), nullable=False)
    mensaje = Column(Text, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    sesion = relationship("SesionModel", backref="mensajes")