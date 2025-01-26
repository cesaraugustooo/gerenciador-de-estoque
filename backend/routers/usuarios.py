from fastapi import APIRouter, HTTPException
from schemas.usuarios import UsuarioResponse, UsuarioSchema
from models.usuarios import UsuarioDB

router = APIRouter(tags=['Usuarios'])

@router.post(path='/usuarios',response_model=UsuarioResponse)
def usuario_create(usuario : UsuarioSchema):
    usuarios = UsuarioDB.create(**usuario.model_dump())
    return usuarios
