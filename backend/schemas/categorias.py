from pydantic import BaseModel

class CategoriaReponse(BaseModel):
    id : int
    nome : str

class CategoriaCreate(BaseModel):
    nome : str

class GetAll(BaseModel):
    categorias : list[CategoriaReponse]