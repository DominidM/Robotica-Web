from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SesionCreateDTO(BaseModel):
    usuario_id: int
    robot_id: int
    fecha_inicio: datetime

class SesionCloseDTO(BaseModel):
    sesion_id: int
    fecha_fin: datetime

class SesionOutDTO(BaseModel):
    id: int
    usuario_id: int
    usuario_nombre: Optional[str] = None
    robot_id: int
    robot_nombre: Optional[str] = None
    fecha_inicio: datetime
    fecha_fin: Optional[datetime] = None

    class Config:
        from_attributes = True