from pydantic import BaseModel
from typing import Literal
from datetime import datetime

class MensajeCreateDTO(BaseModel):
    sesion_id: int
    remitente: Literal['usuario', 'robot']
    mensaje: str

class MensajeOutDTO(BaseModel):
    id: int
    sesion_id: int
    remitente: Literal['usuario', 'robot']
    mensaje: str
    timestamp: datetime

    class Config:
        from_attributes = True