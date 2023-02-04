from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.models import Wishlist, Product, db, User

wishlist_routes = Blueprint( 'wishlists', __name__,  )

# get wishlist for curent user 
@wishlist_routes.route('/')
@login_required
def get_list():
    wishlist = Wishlist.query.filter(Wishlist.user_id == current_user.id).all()
    # for each item in the wishlist, lets find the product that was the item.product_id then call the to dict method on the class we made
    product_list = [Product.query.get(item.product_id).to_dict() for item in wishlist]
   
    return jsonify(product_list)

#Add a product to the wish list
@wishlist_routes.route('/addProduct/<int:product_id>', methods=['POST'] )
@login_required
def add_to_list(product_id):
    added_product = Wishlist(
        product_id = product_id,
        user_id = current_user.id,
    )
    db.session.add(added_product)
    db.session.commit()
    return jsonify('Successfully added product to the wishlist')


# Remove a product from the wishlist
@wishlist_routes.route('/deleteProduct/<int:product_id>', methods=['DELETE'])
# @login_required
def remove_from_list(product_id):
    items = Wishlist.query.filter(Wishlist.user_id == current_user.id and Wishlist.product_id == product_id).all()

    if not items:
        return { 'Errors': [ 'That item on the wishlist does not exist. '] }, 401

    for product in items:
       if product_id == product.product_id:
        db.session.delete(product)
        db.session.commit()
        return jsonify('Successfully removed that product from the list.')
    