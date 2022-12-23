from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.models import Department, Product

product_routes = Blueprint( 'products', __name__,  )

@product_routes.route('/<int:product_id>')
def single_product(product_id):
    product = Product.query.get(product_id)
    json_product = product.to_dict()
    return json_product