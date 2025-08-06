from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RobotDTO(BaseModel):
    id: int
    nombre: str
    identificador_unico: str
    ip_actual: Optional[str] = None
    estado: Optional[str] = None
    descripcion: Optional[str] = None
    fecha_registro: Optional[datetime] = None

    @staticmethod
    def from_entity(robot):
        return RobotDTO(
            id=robot.id,
            nombre=robot.nombre,
            identificador_unico=robot.identificador_unico,
            ip_actual=robot.ip_actual,
            estado=robot.estado,
            descripcion=robot.descripcion,
            fecha_registro=robot.fecha_registro
        )