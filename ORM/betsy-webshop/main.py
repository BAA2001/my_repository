__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import Users, Product, Tag, Transaction, ProductTag
from models import db

db.connect()
db.create_tables([Users, Product, Tag, ProductTag, Transaction])


def search(term):
    return Product.select().where(Product.name.contains(term))


def list_user_products(user_name):
    user = Users.get(Users.name == user_name)
    return Product.select().where(Product.owner == user)


def list_products_per_tag(tag_name):
    products = Product.select().join(ProductTag).join(Tag).where(Tag.name == tag_name)
    return products


def add_product_to_catalog(
    product_name,
    user_name,
    description="No description provided.",
    price=0.0,
    quantity=0,
):
    user = Users.select().where(Users.name == user_name).get()
    new_product = Product.create(
        name=product_name,
        owner=user,
        description=description,
        price=price,
        quantity=quantity,
    )
    db.commit()
    return new_product


def update_stock(product_name, new_quantity):
    product = Product.select().where(Product.name == product_name).get()
    product.quantity = new_quantity
    product.save()
    db.commit()


def purchase_product(product_name, buyer_name, quantity):
    buyer = Users.select().where(Users.name == buyer_name).get()
    product = Product.select().where(Product.name == product_name).get()
    if product.quantity >= quantity:
        product.quantity -= quantity
        product.save()

        transaction = Transaction.create(
            buyer=buyer, product=product, quantity=quantity
        )
        db.commit()
    else:
        return "Transaction failed. Not enough stock available"


def remove_product(product_name):
    product = Product.select().where(Product.name == product_name).get()
    product.delete_instance()
    db.commit()
