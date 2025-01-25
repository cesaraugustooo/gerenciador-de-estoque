from fastapi import APIRouter,HTTPException
from schemas.categorias import * 
from models.categorias import *

router = APIRouter(tags=['Categorias'])

@router.get(path='/categorias',response_model=GetAll)
def get_all():
    categoria = CategoriaDB.select()
    return {'categorias':categoria}

@router.get(path='/categorias/{id}',response_model=CategoriaReponse)
def get(id : int):
    categoria = CategoriaDB.get_or_none(id == CategoriaDB.id)
    if not categoria:
        raise HTTPException(detail='Categoria não encontrada',status_code=404)
    return categoria

@router.post(path='/categorias',response_model=CategoriaReponse)
def create_categoria(categoria : CategoriaCreate):
    categorias = CategoriaDB.create(**categoria.model_dump())
    return categorias

@router.delete(path='/categorias/{id}',response_model=CategoriaReponse)
def delete_categoria(id : int):
    categoria = CategoriaDB.get_or_none(id == CategoriaDB.id)
    categoria.delete_instance()
    return categoria

@router.put(path='/categoria/{id}',response_model=CategoriaReponse)
def update_catgeoria(id : int, update : CategoriaCreate):
    categoria = CategoriaDB.get_or_none(id == CategoriaDB.id)
    categoria.nome = update.nome
    categoria.save()
    return categoria
