from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.models import Review, Product, db, User
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
    users = User.query.all()
    list = []
    if product_reviews:

        for review in product_reviews:
            # Grab user review relationship of user object, then the review dictionary and update them together
            # to have one big dictionary of combined dictionaries
            userReview = review.review_to_user.to_dict()
            review = review.to_dict()
            userReview.update(review)
            # push or append the newly updated dict into a list to store all of our dictionaries
            list.append(userReview)
            
        return jsonify(list)

# Add a review to a product
@review_routes.route('/<int:product_id>', methods=['POST'])
@login_required
def add_review(product_id):
    form = review_form()
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data
    if form.validate_on_submit():
        new_review = Review(
            product_id = product_id,
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
    # oldReview = review.to_dict()
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data
   
    if review and form.validate_on_submit():
        # print(' THIS PRINT NEVER PRINTS?????????')
        review.user_id = data['user_id']
        review.rating = data['rating']
        review.comment = data['comment']
        db.session.commit()
        return jsonify(review.to_dict())

    if not review:
        return { 'errors ': [ 'That review does not exist. '] }, 401
    
    else:
        return jsonify(form.errors)


# Get review by review_id
@review_routes.route('/get/<int:review_id>')
def get_review(review_id):
    return Review.query.get(review_id).to_dict()
 