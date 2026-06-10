from peewee import SqliteDatabase, Model, CharField, IntegerField

db = SqliteDatabase("vehicles.db")

class Vehicle(Model):
    make = CharField()
    model = CharField()
    year = IntegerField()
    mpg = IntegerField()
    category = CharField()
    tco_10yr = IntegerField()

    class Meta:
        database = db

db.connect()
db.create_tables([Vehicle])

Vehicle.create(
    make = "Honda", model = "Civic", year = 2020, mpg = 33, category = "Van", tco_10yr = 20634)

Vehicle.create(
    make = "Chevrolet", model = "Blazer", year = 2020, mpg = 21, category = "SUV", tco_10yr = 32961.43)

Vehicle.create(
    make = "Subaru", model = "Outback", year = 2021, mpg = 29, category = "SUV", tco_10yr = 25701.97)

for v in Vehicle.select():
    print(v.make, v.model, v.mpg)