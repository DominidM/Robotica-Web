from datetime import datetime
from typing import Optional, Literal

class Mensaje:
    def __init__(
        self,
        id: Optional[int],
        sesion_id: int,
        remitente: Literal["usuario", "robot"],
        mensaje: str,
        timestamp: Optional[datetime] = None
    ):
        self.id = id
        self.sesion_id = sesion_id
        self.remitente = remitente
        self.mensaje = mensaje
        self.timestamp = timestamp