from peewee import *
import datetime

db = SqliteDatabase('./db/green_controller.db')

class Measurements(Model):
    id = PrimaryKeyField()
    temperature = IntegerField()
    humidity = IntegerField()
    created_at = DateField(default= datetime.datetime.now().astimezone())

    class Meta:
        database = db
        db_table = 'Measurements'
        order_by = ('id',)

db.connect()
db.create_tables([Measurements])