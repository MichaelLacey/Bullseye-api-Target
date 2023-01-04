const GET_USERS_CART = 'get/cart'
const ADD_TO_CART = 'add/cart'
const DELETE_TO_CART = 'delete/cart'



/* ___________ A C T I O N S   ___________ */
// Get cart items
export const getCartItems = (products) => {
    return {
        type: GET_USERS_CART,
        products
    };
};
// Add a product to a cart
export const addCartItem = (product) => {
    return {
        type:ADD_TO_CART,
        product
    };
};

// Remove a product to a cart
export const deleteCartItem = (product) => {
    return{
        type:DELETE_TO_CART,
        product
    };
};



/* ___________ T H U N K S   ___________ */

// Get users products in cart
export const getUsersCartThunk = () => async(dispatch) => {
    const response = await fetch('/api/cart');
    const cart = await response.json();
    dispatch(getCartItems(cart));
};






/* ___________ R E D U C E R ___________ */
const cartReducer = (state = {}, action) => {
    let newState = {};
    switch (action.type) {
        
        case GET_USERS_CART:
            action.products.forEach(ele => newState[ele.id] = ele)
            return newState

        case ADD_TO_CART:
            newState = { ...state }
            newState[action.product.id] = action.product
            return newState
        
        case DELETE_TO_CART:
            newState = { ...state }
            delete newState[action.product.id] 
            return newState

        default:
            return state;
    };
};

export default cartReducer;