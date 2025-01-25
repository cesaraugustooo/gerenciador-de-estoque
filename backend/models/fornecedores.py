from peewee import CharField,IntegerField,ForeignKeyField,Model,AutoField,DecimalField
from config.database import database

class FornecedorDB(Model):
    id = AutoField()
    nome = CharField()
    email = CharField()
    numero = CharField()

    class Meta:
        database = database

