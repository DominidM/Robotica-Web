from pydantic import BaseModel

class RolCreateDTO(BaseModel):
    nombre: str
    email: str
    password: str
    fecha_registro: str
    rol_id: int
    registro_key: str

class RolOutDTO(BaseModel):
    id: int
    nombre: str
    email: str
    fecha_registro: str
    rol_id: int
    registro_key: str

    class Config:
        orm_mode = True