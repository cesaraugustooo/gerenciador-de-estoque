from fastapi import APIRouter, HTTPException
from schemas.produtos import ProdutoReponse, ProdutoCreate
from models.produtos import ProdutosDB

router = APIRouter(tags=['Produtos'])

@router.get(path='/produtos', response_model=list[ProdutoReponse])
def get_all():
    produtos = ProdutosDB.select()
    return produtos

@router.get(path='/produtos/{id}', response_model=ProdutoReponse)
def get(id: int):
    produto = ProdutosDB.get_or_none(ProdutosDB.id == id)
    if not produto:
        raise HTTPException(detail='Produto não encontrado', status_code=404)
    return produto

@router.post(path='/produtos',response_model=ProdutoReponse)
def produtos_create(produto : ProdutoCreate):
    produtos = ProdutosDB.create(**produto.model_dump())
    return produtos

@router.delete(path='/produtos/{id}', response_model=ProdutoReponse)
def delete_produto(id: int):
    produto = ProdutosDB.get_or_none(ProdutosDB.id == id)
    if not produto:
        raise HTTPException(detail='Produto não encontrado', status_code=404)
    produto.delete_instance()
    return produto

@router.put(path='/produtos/{id}', response_model=ProdutoReponse)
def update_produto(id: int, update: ProdutoCreate):
    produto = ProdutosDB.get_or_none(ProdutosDB.id == id)
    if not produto:
        raise HTTPException(detail='Produto não encontrado', status_code=404)
    produto.nome = update.nome
    produto.preco = update.preco
    produto.fornecedor_id = update.fornecedor_id
    produto.categoria_id = update.categoria_id
    produto.save()
    return produto
