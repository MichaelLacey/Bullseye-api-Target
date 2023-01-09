from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.models import Department, Product, Cart_Product, db, User

cart_routes = Blueprint( 'carts', __name__,  )

@cart_routes.route('')
@login_required
def get_cart_products():
    #Grab user's products through the joined table by keying into products of user
    user = User.query.get(current_user.id).products
    # Each model has a to_dict() method to put all the info into a dictionary(pojo)
    return jsonify( [ product.to_dict() for product in user] )


    
  

# Add product to a users cart 
@cart_routes.route('/add/<int:product_id>', methods=['POST'])
@login_required
def add_cart_product(product_id):
    # Get all users products
    users_cart = User.query.get(current_user.id).products
    # grab the user 
    user = User.query.get(current_user.id)
    # grab product by id
    product = Product.query.get(product_id)
    # add the product to the users product list
    # Add the product into the database then commit so it saves
    user.products.append(product)
    db.session.add(user)
    db.session.commit()
    cart = [ product.to_dict() for product in users_cart ]
    return jsonify(cart)
    
# Delete a product from a users cart
@cart_routes.route('/delete/<int:product_id>', methods=['DELETE'])
@login_required
def delete_cart_product(product_id):
    # Get current user
    user = User.query.get(current_user.id)
    #Get product then remove that from user's products
    product = Product.query.get(product_id)
    users_products = user.products
    # loop through the users products to find a matching id
    for product in users_products:
        if product_id == product.id:
            user.products.remove(product)
            db.session.add(user)
            db.session.commit()
            return jsonify('Product successfully deleted from cart.')
    # If there is no product that matches the product id
    return jsonify("Couldn't find that product in your cart.")

# Checkout the cart, essentially delete all the items from the cart 
@cart_routes.route( '/checkout' )
@login_required
def checkout_Cart():
    users_products = User.query.get(current_user.id).products
    user = User.query.get(current_user.id)

    for product in users_products:
        user.products.remove(product)
        db.session.add(user)
        db.session.commit()

    user_products = User.query.get(current_user.id).products
    userr = User.query.get(current_user.id)

    for product in user_products:
        userr.products.remove(product)
        db.session.add(userr)
        db.session.commit()

    return jsonify('Cart has successfully been checked out.')