# modules/public/emociones/infrastructure/model/emocion_model.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from modules.database import Base

class EmocionModel(Base):
    __tablename__ = "emociones"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sesion_id = Column(Integer, ForeignKey("sesiones.id"), nullable=True)  
    emocion = Column(String(50), nullable=True)
    confianza = Column(Float, nullable=True)
    imagen_url = Column(String(255), nullable=True)
    timestamp = Column(DateTime, nullable=True)

    # Relación con sesiones
    sesion = relationship("SesionModel", backref="emociones")