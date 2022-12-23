from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.models import Department, Product, Cart_Product, db

cart_routes = Blueprint( 'carts', __name__,  )

@cart_routes.route('')
def get_cart_products():
    cart = db.session.query(Cart_Product).all()
    return jsonify(cart)


@cart_routes.route('/add/<int:product_id>')
def add_cart_product(product_id):
    cart = db.session.query(Cart_Product).all()
    print('This is my cart', cart)
    product = Product.query.get(product_id)
    json_product = product.to_dict()
    print('product', product)
    return ' in this add route '
    