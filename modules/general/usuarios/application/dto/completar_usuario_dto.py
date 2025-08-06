from pydantic import BaseModel

class CompletarUsuarioDTO(BaseModel):
    registro_key: str
    email: str
    password: str