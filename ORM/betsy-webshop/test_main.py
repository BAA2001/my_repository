from models import User, Product, Tag, Transaction, ProductTag
from models import db
from main import (
    search,
    list_user_products,
    list_products_per_tag,
    add_product_to_catalog,
    update_stock,
    purchase_product,
)


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
