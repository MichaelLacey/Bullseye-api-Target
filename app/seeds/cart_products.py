from app.models import db, User, Product, environment, SCHEMA

def seed_cart_products():
    demo_user = User.query.get(1)
    marnie = User.query.get(2)
    product_list = []
    for i in range(1, 6):
        # Query for the first 5 products
        product = Product.query.get(i)
        product_list.append(product)


    for i in product_list:
        demo_user.products.append(i)
        marnie.products.append(i)
        db.session.add(demo_user)
        db.session.add(marnie)


    db.session.commit()


def undo_cart_products():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.cart_products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM departments")
    db.session.commit()