import peewee

db = peewee.SqliteDatabase("betsy.db")


class BaseModel(peewee.Model):
    class Meta:
        database = db


class User(BaseModel):
    name = peewee.CharField()
    address = peewee.CharField()
    billing_info = peewee.CharField()


class Tag(BaseModel):
    name = peewee.CharField()


class Product(BaseModel):
    name = peewee.CharField()
    description = peewee.CharField()
    price = peewee.DecimalField()
    quantity = peewee.IntegerField()
    owner = peewee.ForeignKeyField(User, backref="products")
    tags = peewee.ManyToManyField(Tag, backref="products")


class ProductTag(BaseModel):
    product = peewee.ForeignKeyField(Product)
    tag = peewee.ForeignKeyField(Tag)


class Transaction(BaseModel):
    buyer = peewee.ForeignKeyField(User, backref="purchases")
    product = peewee.ForeignKeyField(Product)
    quantity = peewee.IntegerField()
