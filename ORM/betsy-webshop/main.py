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


def test_queries():
    # Create example data
    user1 = User.create(name="John Doe", address="123 Main St", billing_info="Visa 200")
    user2 = User.create(name="Jane Smith", address="456 Park Ave", billing_info="MC 56")
    product1 = Product.create(
        name="Handmade sweater",
        description="Warm and cozy sweater made from 100% wool.",
        price=50.00,
        quantity=5,
        owner=user1,
    )
    product2 = Product.create(
        name="Handmade scarf",
        description="Soft and warm scarf made from 100% alpaca.",
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
    results = search("sweater")
    assert len(results) == 1
    assert results[0].name == "Handmade sweater"

    # Test list user products query
    results = list_user_products("John Doe")
    assert len(results) == 1
    assert results[0].name == "Handmade sweater"

    # Test list products per tag query
    results = list_products_per_tag("Winter")
    assert len(results) == 1
    assert results[0].name == "Handmade sweater"

    # Test add product to catalog query
    add_product_to_catalog("Handmade scarf", "John Doe")
    results = list_user_products("John Doe")
    assert len(results) == 2
    assert results[1].name == "Handmade scarf"

    # Test update stock query
    update_stock("Handmade sweater", 10)
    results = Product.get(Product.name == "Handmade sweater")
    assert results.quantity == 10

    # Test purchase product query
    purchase_product("Handmade sweater", "Jane Smith", 2)
    results = Product.get(Product.name == "Handmade sweater")
    assert results.quantity == 8
    results = Transaction.select().where(Transaction.product == product1)
    assert len(results) == 1
    assert results[0].quantity


test_queries()
