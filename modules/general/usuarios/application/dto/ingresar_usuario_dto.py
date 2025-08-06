from pydantic import BaseModel

class UsuarioCreateRobotDTO(BaseModel):
    nombre: str
    registro_key: str
    rol_id: int