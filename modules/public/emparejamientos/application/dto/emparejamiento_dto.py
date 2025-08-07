from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EmparejamientoCreateDTO(BaseModel):
    usuario_id: int
    robot_id: int
    fecha_inicio: datetime
    estado: Optional[str] = None

class EmparejamientoUpdateDTO(BaseModel):
    id: int
    fecha_fin: Optional[datetime] = None
    estado: Optional[str] = None

class EmparejamientoOutDTO(BaseModel):
    id: int
    usuario_id: int
    robot_id: int
    fecha_inicio: datetime
    fecha_fin: Optional[datetime]
    estado: Optional[str]
    usuario_nombre: Optional[str] = None
    robot_nombre: Optional[str] = None

    class Config:
        from_attributes = True