from pydantic import BaseModel

class RolCreateDTO(BaseModel):
    nombre: str

class RolOutDTO(BaseModel):
    id: int
    nombre: str

    class Config:
        from_attributes = True  