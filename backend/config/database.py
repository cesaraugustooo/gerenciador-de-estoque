from peewee import SqliteDatabase

database = SqliteDatabase('database.db')

def connect_database():
    database.connect
    from models.produtos import ProdutosDB
    from models.categorias import CategoriaDB
    from models.fornecedores import FornecedorDB
    database.create_tables([ProdutosDB,CategoriaDB,FornecedorDB])

def end_connect():
    database.close()