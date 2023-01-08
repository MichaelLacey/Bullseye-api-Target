const GET_PRODUCT_REVIEWS = 'get/reviews/product'
const EDIT_REVIEW = 'edit/review/product'
const GET_ONE_REVIEW = 'get/review/idfromurl'
const DELETE_REVIEW = 'delete/review'
const ADD_REVIEW = 'add/review'

/* ___________ A C T I O N S   ___________ */
export const getReviewsForProduct = (reviews) => {
    return {
        type: GET_PRODUCT_REVIEWS,
        reviews
    };
};

export const editReviewAction = (review) => {
    return {
        type: EDIT_REVIEW,
        review
    };
};

export const getOneReview = (review) => {
    return {
        type: GET_ONE_REVIEW,
        review
    };
};
export const deleteReview = (reviewId) => {
    return {
        type: DELETE_REVIEW,
        reviewId
    }
}
export const addReviewAction = (review) => {
    return {
        type: ADD_REVIEW,
        review
    }
}


/* ___________ T H U N K S   ___________ */

// Get reviews for a product 
export const getProductReviewsThunk = (productId) => async (dispatch) => {
    const response = await fetch(`/api/reviews/${productId}`);
    const reviews = await response.json();
    dispatch(getReviewsForProduct(reviews));
};

// Edit a review
export const editReviewThunk = (review, reviewId) => async (dispatch) => {
    const { comment, rating } = review;

    const response = await fetch(`/api/reviews/${reviewId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(
            {
                comment,
                rating
            }
        )
    })
    if (response.ok) {
        const newReview = await response.json();

        dispatch(editReviewAction(newReview));
        return newReview
    };
};
// Delete a review for a product
export const deleteReviewThunk = (reviewId) => async (dispatch) => {
    const response = await fetch(`/api/reviews/delete/${reviewId}`, { method: 'DELETE' });
    if (response.ok) dispatch(deleteReview(reviewId))
};

// Get one review by url review id
export const getOneReviewThunk = (reviewId) => async (dispatch) => {
    const response = await fetch(`/api/reviews/get/${reviewId}`);
    const review = await response.json();
    dispatch(getOneReview(review));
    return review;
};
// Create a review
export const createReviewThunk = (review, productId) => async (dispatch) => {
    const { user_id, comment, rating } = review;
    const response = await fetch(`/api/reviews/${productId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            user_id,
            comment,
            rating,
        })
    });

    if (response.ok) {
        const newReview = await response.json();
        dispatch(addReviewAction(newReview));
        return newReview;
    };
};
/* ___________ R E D U C E R ___________ */
const reviewsReducer = (state = {}, action) => {
    let newState = {};

    switch (action.type) {

        case GET_PRODUCT_REVIEWS:
            action.reviews.forEach(ele => newState[ele.id] = ele)
            return newState

        case EDIT_REVIEW:
            newState = { ...state }
            newState[action.review.id] = action.review
            return newState

        case GET_ONE_REVIEW:
            return action.review

        case DELETE_REVIEW:
            newState = { ...state }
            delete newState[action.reviewId]
            return newState

        case ADD_REVIEW:
            newState = { ...state }
            newState[action.review.id] = action.review
            return newState

        default:
            return state


    };
};

export default reviewsReducer;