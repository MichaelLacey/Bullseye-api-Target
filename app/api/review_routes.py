from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.models import Review, Product, db
from app.forms.review_form import review_form

review_routes = Blueprint( 'reviews', __name__,  )

# Get all reviews
@review_routes.route('')
def all_routes():
    reviews = Review.query.all()
    reviews_dict = [ review.to_dict() for review in reviews ]
    return jsonify(reviews_dict)

# Get reviews for a product
@review_routes.route('/<int:product_id>')
def reviews_for_product(product_id):
    product_reviews = Review.query.filter(Review.product_id == product_id)
    if product_reviews:
        reviews_dict = [ review.to_dict() for review in product_reviews]
        return jsonify(reviews_dict)


# Add a review to a product
@review_routes.route('/<int:product_id>', methods=['POST'])
@login_required
def add_review(product_id):
    form = review_form()
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data
    if form.validate_on_submit():
        new_review = Review(
            product_id = data['product_id'],
            user_id = data['user_id'],
            rating = data['rating'],
            comment = data['comment']
        )
        db.session.add(new_review)
        db.session.commit()
        return jsonify(new_review.to_dict())
    return jsonify(form.errors)

# Delete a review for a product 
@review_routes.route('/delete/<int:review_id>', methods=['DELETE'])
@login_required
def delete_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        return { 'errors ': [ 'That review does not exist. '] }, 401
    db.session.delete( review )
    db.session.commit()
    return jsonify( 'Successfully deleted your review' )


# Edit a review for a product 
@review_routes.route('/<int:review_id>', methods=['PUT'])
@login_required
def edit_review(review_id):
    form = review_form()
    review = Review.query.get(review_id)
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data
    print('review==============================', review.comment)
    if review and form.validate_on_submit():
        review.product_id = data['product_id']
        review.user_id = data['user_id']
        review.rating = data['rating']
        review.comment = data['comment']
        db.session.commit()
        return (review.to_dict())

    if not review:
        return { 'errors ': [ 'That review does not exist. '] }, 401
    
    else:
        return jsonify(form.errors)