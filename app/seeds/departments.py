from app.models import db, Department, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_departments():
    electronics = Department(name='Electronics', image_url='https://target.scene7.com/is/image/Target/GUEST_ff3c311a-e99e-4834-bac4-07055eb95f5d?wid=325&hei=325&qlt=80&fmt=pjpeg')
    household_essentials = Department(name='Household Essentials', image_url='https://target.scene7.com/is/image/Target/GUEST_3db36f68-f2c9-4561-a858-68d6584366c0?wid=325&hei=325&qlt=80&fmt=pjpeg')
    sports_outdoors = Department(name='Sports & Outdoors', image_url='https://target.scene7.com/is/image/Target/GUEST_6949369e-0e6c-4cc6-8451-563c9aa68ceb?qlt=85&fmt=webp&hei=324&wid=324&fit=crop')
    movies = Department(name='Movies', image_url='https://target.scene7.com/is/image/Target/GUEST_c93ceddc-bbe6-4184-9bfb-6526855b020c?wid=325&hei=325&qlt=80&fmt=pjpeg')
    personal_care = Department(name='Personal Care', image_url='https://target.scene7.com/is/image/Target/GUEST_1bcea319-4a69-42a9-9639-ed05aadf5496?wid=325&hei=325&qlt=80&fmt=pjpeg')
    kitchen_dining = Department(name='Kitchen & Dining', image_url='https://target.scene7.com/is/image/Target/GUEST_2758701a-9d26-46e8-ad4f-620eb1c1ccb6?qlt=85&fmt=webp&hei=325&wid=325')

    db.session.add(electronics)
    db.session.add(household_essentials)
    db.session.add(sports_outdoors)
    db.session.add(movies)
    db.session.add(personal_care)
    db.session.add(kitchen_dining)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_departments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.departments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM departments")
        
    db.session.commit()