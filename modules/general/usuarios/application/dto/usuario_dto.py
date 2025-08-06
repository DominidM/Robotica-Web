from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class UsuarioOutDTO(BaseModel):
    id: int
    nombre: str
    email: Optional[str] = None   # <-- Hazlo opcional
    fecha_registro: datetime | None = None
    rol_id: int | None = None
    rol_nombre: str | None = None        # <-- AGREGADO
    registro_key: str | None = None

    class Config:
        from_attributes = True