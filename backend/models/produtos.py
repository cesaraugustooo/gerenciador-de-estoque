from peewee import CharField,IntegerField,ForeignKeyField,Model,AutoField,DecimalField
from models.categorias import CategoriaDB
from models.fornecedores import FornecedorDB
from models.usuarios import UsuarioDB
from config.database import database

class ProdutosDB(Model):
    id = AutoField()
    nome = CharField()
    preco = DecimalField()
    fornecedor_id = ForeignKeyField(FornecedorDB,backref='fornecedor')
    categoria_id = ForeignKeyField(CategoriaDB, backref='categoria')
    usuario_id = ForeignKeyField(UsuarioDB,backref='usuario')
    class Meta:
        database = database


