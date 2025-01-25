from peewee import CharField,Model,AutoField
from config.database import database

class CategoriaDB(Model):
    id = AutoField()
    nome = CharField()

    class Meta:
        database = database