from pydantic import BaseModel

class RolCreateDTO(BaseModel):
    id: str

class RolOutDTO(BaseModel):
    id: int
    
    class Config:
        orm_mode = True