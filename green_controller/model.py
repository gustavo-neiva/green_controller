from peewee import *
import datetime

db = SqliteDatabase('./db/green_controller.db')


class Measurements(Model):
    temperature = IntegerField()
    humidity = IntegerField()
    sensor_id = IntegerField()
    created_at = DateField(default=datetime.datetime.now().astimezone())

    class Meta:
        database = db
        db_table = 'Measurements'
        order_by = ('id',)


db.connect()
db.create_tables([Measurements])
