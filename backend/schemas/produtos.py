from pydantic import BaseModel,Fiel
from schemas.categorias import *
from schemas.fornecedores import *


class ProdutoReponse(BaseModel):
    id : int
    nome : str
    preco : float
    fornecedor_id : FornecedorReponse
    categoria_id : CategoriaReponse

class ProdutoCreate(BaseModel):
    nome : str
    preco : float
    fornecedor_id : int
    categoria_id : int

