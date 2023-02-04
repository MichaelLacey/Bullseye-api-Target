const get_wishlist = 'get/wishlist';
const add_to_wishlist = 'add/wishlist';
const delete_from_wishlist = 'delete/wishlist';

/* ___________ A C T I O N S   ___________ */
// get items in a persons wishlist
export const getWishlistAction = (products) => {
    return {
        type: get_wishlist,
        products
    };
};

// Add item to wishlist
export const addToWishlistAction = (product) => {
    return {
        type: add_to_wishlist,
        product
    };
};

// Delete item from the wishlist
export const deleteFromWishlistAction = (productId) => {
    return {
        type: delete_from_wishlist,
        productId
    };
};

/* ___________ T H U N K S   ___________ */

// get wishlist
export const getWishlistThunk = () => async (dispatch) => {
    const response = await fetch('/api/wishlist/');
    const products = await response.json();
    dispatch(getWishlistAction(products));
};

// add to wishlist
export const addToWishlistThunk = (productId) => async (dispatch) => {
    const response = await fetch(`/api/wishlist/addProduct/${productId}`, { method: 'POST' });

    if (response.ok) {
        const product = await response.json();
        dispatch(addToWishlistAction(product));
    };
};

// Delete from wishlist 
export const deleteFromWishlistThunk = (wishlistId) => async (dispatch) => {
    const response = await fetch(`/api/wishlist/deleteProduct/${wishlistId}`, { method: 'DELETE' });
    if (response.ok) dispatch(deleteFromWishlistAction(wishlistId));
};

/* ___________ R E D U C E R ___________ */
const wishlistReducer = (state = {}, action) => {
    let newState = {};
    switch (action.type) {

        case get_wishlist:
            action.products.forEach(ele => newState[ele.id] = ele)
            return newState

        case add_to_wishlist:
            newState = { ...state }
            newState[action.product.id] = action.product
            return newState

        case delete_from_wishlist:
            newState = { ...state }
            delete newState[action.productId]
            return newState

        default:
            return state;
    };
};

export default wishlistReducer;