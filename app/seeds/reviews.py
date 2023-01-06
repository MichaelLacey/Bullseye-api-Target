from app.models import db, Review, environment, SCHEMA


def seed_reviews():
    review1 = Review( product_id=1, user_id=1, rating=5, comment='This is such a good product. I use it everyday and my kids love it! It looks so good in my living room with my other decorations.' )
    review2 = Review( product_id=2, user_id=1, rating=3, comment='This is such a good product. I use it everyday and my kids love it! It looks so good in my living room with my other decorations.' )

    db.session.add(review1)
    db.session.add(review2)
    # db.session.add()
    # db.session.add()
    # db.session.add()
    # db.session.add()
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the reviews table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM reviews")
        
    db.session.commit()