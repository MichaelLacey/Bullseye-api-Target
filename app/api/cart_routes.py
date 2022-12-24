from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.models import Department, Product, Cart_Product, db, User

cart_routes = Blueprint( 'carts', __name__,  )

@cart_routes.route('')
@login_required
def get_cart_products():
    user = User.query.get(current_user.id).products
    return jsonify( [ product.to_dict() for product in user] )


    
  


@cart_routes.route('/add/<int:product_id>', methods=['POST'])
@login_required
def add_cart_product(product_id, user_id):
    print('current user', current_user.id)
    cart = db.session.query(Cart_Product).filter(userid == current_user.id )
    product = Product.query.get(product_id)
    cart.append(product.to_dict())
    db.session.commit()
    return jsonify(cart)
    