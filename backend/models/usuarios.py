from peewee import CharField,Model,AutoField
from config.database import database

class UsuarioDB(Model):
    id = AutoField()
    nome = CharField()
    email = CharField()
    senha = CharField()

    class Meta:
        database = database