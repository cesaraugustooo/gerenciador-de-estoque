from peewee import SqliteDatabase

database = SqliteDatabase('database.db')

def connect_database():
    database.connect
    from models.produtos import ProdutosDB
    from models.categorias import CategoriaDB
    from models.fornecedores import FornecedorDB
    from models.usuarios import UsuarioDB
    database.create_tables([ProdutosDB,CategoriaDB,FornecedorDB,UsuarioDB])

def end_connect():
    database.close()