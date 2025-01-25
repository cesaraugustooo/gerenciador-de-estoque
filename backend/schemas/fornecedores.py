from pydantic import BaseModel

class FornecedorReponse(BaseModel):
    id : int
    nome : str
    email : str
    numero : str

class FornecedorCreate(BaseModel):
    nome : str
    email : str
    numero : str

