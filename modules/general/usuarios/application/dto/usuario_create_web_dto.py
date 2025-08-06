from pydantic import BaseModel

class UsuarioCreateWebDTO(BaseModel):
    nombre: str
    email: str
    rol_id: int
    registro_key: str | None = None