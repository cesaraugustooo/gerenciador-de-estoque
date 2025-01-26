from pydantic import BaseModel


class UsuarioSchema(BaseModel):
    id: int
    nome: str
    email: str
    senha: str

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str

