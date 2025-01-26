from pydantic import BaseModel
from schemas.categorias import *
from schemas.fornecedores import *
from schemas.usuarios import *

class ProdutoReponse(BaseModel):
    id : int
    nome : str
    preco : float
    fornecedor_id : FornecedorReponse
    categoria_id : CategoriaReponse
    usuario_id : UsuarioResponse    

class ProdutoCreate(BaseModel):
    nome : str
    preco : float
    fornecedor_id : int
    categoria_id : int
    usuario_id : int

