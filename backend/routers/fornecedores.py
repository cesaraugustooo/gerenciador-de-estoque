from fastapi import APIRouter, HTTPException
from schemas.fornecedores import FornecedorCreate, FornecedorReponse
from models.fornecedores import FornecedorDB

router = APIRouter(tags=['Fornecedores'])

@router.get('/fornecedores', response_model=list[FornecedorReponse])
def get_all_fornecedores():
    fornecedores = list(FornecedorDB.select())
    return fornecedores

@router.get('/fornecedores/{id}', response_model=FornecedorReponse)
def get_fornecedor(id: int):
    fornecedor = FornecedorDB.get_or_none(FornecedorDB.id == id)
    if not fornecedor:
        raise HTTPException(detail='Fornecedor não encontrado', status_code=404)
    return fornecedor

@router.post('/fornecedores', response_model=FornecedorReponse)
def create_fornecedor(fornecedor: FornecedorCreate):
    novo_fornecedor = FornecedorDB.create(**fornecedor.model_dump())
    return novo_fornecedor

@router.delete('/fornecedores/{id}', response_model=FornecedorReponse)
def delete_fornecedor(id: int):
    fornecedor = FornecedorDB.get_or_none(FornecedorDB.id == id)
    if not fornecedor:
        raise HTTPException(detail='Fornecedor não encontrado', status_code=404)
    fornecedor.delete_instance()
    return fornecedor

@router.put('/fornecedores/{id}', response_model=FornecedorReponse)
def update_fornecedor(id: int, update: FornecedorCreate):
    fornecedor = FornecedorDB.get_or_none(FornecedorDB.id == id)
    if not fornecedor:
        raise HTTPException(detail='Fornecedor não encontrado', status_code=404)
    
    fornecedor.nome = update.nome
    fornecedor.email = update.email
    fornecedor.numero = update.numero
    fornecedor.usuario_id = update.usuario_id
    fornecedor.save()
    return fornecedor
