from pydantic import BaseModel

class RolCreateDTO(BaseModel):
    nombre: str
    descripcion: str

class RolOutDTO(BaseModel):
    id: int
    nombre: str
    descripcion: str

    class Config:
        orm_mode = True