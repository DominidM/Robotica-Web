from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EmocionCreateDTO(BaseModel):
    sesion_id: int  # ✅ Cambiar de session_id a sesion_id
    emocion: str
    confianza: Optional[float] = None
    imagen_url: Optional[str] = None

class EmocionOutDTO(BaseModel):
    id: int
    sesion_id: int  # ✅ Cambiar de session_id a sesion_id
    emocion: str
    confianza: Optional[float]
    imagen_url: Optional[str]
    timestamp: datetime

    class Config:
        from_attributes = True