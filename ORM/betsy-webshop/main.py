__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import User, Product, Tag, Transaction, ProductTag
from models import db


def search(term):
    return Product.select().where(Product.name.contains(term))


def list_user_products(user_name):
    user = User.get(User.name == user_name)
    return Product.select().where(Product.owner == user)


def list_products_per_tag(tag_name):
    products = Product.select().join(ProductTag).join(Tag).where(Tag.name == tag_name)
    return products


def add_product_to_catalog(product_name, user_name):
    product = Product.get(Product.name == product_name)
    user = User.get(User.name == user_name)
    product.owner = user
    product.save()
    db.commit()


def update_stock(product_name, new_quantity):
    product = Product.get(Product.name == product_name)
    product.quantity = new_quantity
    product.save()
    db.commit()


def purchase_product(product_name, buyer_name, quantity):
    buyer = User.get(User.name == buyer_name)
    product = Product.get(Product.name == product_name)
    # decrease stock quantity
    product.quantity -= quantity
    product.save()
    # create transaction
    transaction = Transaction(buyer=buyer, product=product, quantity=quantity)
    transaction.save()
    db.commit()


def remove_product(product_name):
    product = Product.get(Product.name == product_name)
    product.owner = None
    product.save()
    db.commit()


def populate_test_database():
    # Create example data
    user1 = User.create(name="Bilal", address="123 street", billing_info="Visa 200")
    user2 = User.create(name="Rachid", address="456 street", billing_info="MC 56")
    product1 = Product.create(
        name="Jacket",
        description="Warm and cozy.",
        price=50.00,
        quantity=5,
        owner=user1,
    )
    product2 = Product.create(
        name="Scarf",
        description="Soft and warm.",
        price=30.00,
        quantity=3,
        owner=user2,
    )
    tag1 = Tag.create(name="Handmade")
    tag2 = Tag.create(name="Winter")
    ProductTag.create(product=product1, tag=tag1)
    ProductTag.create(product=product1, tag=tag2)
    ProductTag.create(product=product2, tag=tag1)

    # Test search products query
    results = search("Jacket")
    assert len(results) == 1
    assert results[0].name == "Jacket"

    # Test list user products query
    results = list_user_products("Bilal")
    assert len(results) == 1
    assert results[0].name == "Jacket"

    # Test list products per tag query
    results = list_products_per_tag("Winter")
    assert len(results) == 1
    assert results[0].name == "Jacket"

    # Test add product to catalog query
    add_product_to_catalog("Scarf", "Bilal")
    results = list_user_products("Bilal")
    assert len(results) == 2
    assert results[1].name == "Scarf"

    # Test update stock query
    update_stock("Jacket", 10)
    results = Product.get(Product.name == "Jacket")
    assert results.quantity == 10

    # Test purchase product query
    purchase_product("Jacket", "Rachid", 2)
    results = Product.get(Product.name == "Jacket")
    assert results.quantity == 8
    results = Transaction.select().where(Transaction.product == product1)
    assert len(results) == 1
    assert results[0].quantity


populate_test_database()
