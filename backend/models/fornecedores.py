from peewee import CharField,IntegerField,ForeignKeyField,Model,AutoField,DecimalField
from config.database import database
from models.usuarios import UsuarioDB

class FornecedorDB(Model):
    id = AutoField()
    nome = CharField()
    email = CharField()
    numero = CharField()
    usuario_id = ForeignKeyField(UsuarioDB,backref='usuarioo')

    class Meta:
        database = database
