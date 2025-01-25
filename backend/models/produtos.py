from peewee import CharField,IntegerField,ForeignKeyField,Model,AutoField,DecimalField
from models.categorias import CategoriaDB
from models.fornecedores import FornecedorDB
from config.database import database

class ProdutosDB(Model):
    id = AutoField()
    nome = CharField()
    preco = DecimalField()
    fornecedor_id = ForeignKeyField(FornecedorDB,backref='fornecedor')
    categoria_id = ForeignKeyField(CategoriaDB, backref='categoria')

    class Meta:
        database = database


