const GET_PRODUCTS_BY_DEPT = 'get/department/products'
const GET_PRODUCT_BY_DEPT = 'get/department/product'

/* ___________ A C T I O N S   ___________ */
export const getProducts = (products) => {
    return {
        type: GET_PRODUCTS_BY_DEPT,
        products
    };
}
export const getProduct = (product) => {
    return {
        type: GET_PRODUCT_BY_DEPT,
        product
    };
}

/* ___________ T H U N K S   ___________ */
// Get products for department 
export const getProductsThunk = (departmentId) => async(dispatch) => {
    const response = await fetch(`/api/departments/${departmentId}/products`)
    const products = await response.json()
    dispatch(getProducts(products));
};

// Get single product
export const getProductThunk = (productId) => async(dispatch) => {
    const response = await fetch(`/api/products/${productId}`);
    const product = await response.json();
    dispatch(getProduct(product))
};

/* ___________ R E D U C E R ___________ */
const productsReducer = (state = {}, action) => {
    let newState = {};
    switch (action.type) {

        case GET_PRODUCTS_BY_DEPT:
            action.products.forEach(ele => newState[ele.id] = ele)
            return newState
    
        case GET_PRODUCT_BY_DEPT:
            newState[action.product.id] = action.product
            return newState

        default:
            return state;
    }
}

export default productsReducer;