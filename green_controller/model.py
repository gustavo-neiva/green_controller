import peewee
import datetime

db = peewee.SqliteDatabase('./db/green_controller.db')

class Measurements(peewee.Model):
    id = peewee.IntegerField(unique=True)
    temperature = peewee.IntegerField()
    humidity = peewee.IntegerField()
    created_at = peewee.DateField(default= datetime.datetime.now().astimezone())

    class Meta:
        database = db
        db_table = 'Measurements'
        order_by = ('id',)


peewee.create_model_tables([Measurements])