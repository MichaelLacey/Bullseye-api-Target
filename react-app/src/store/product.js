const GET_PRODUCTS_BY_DEPT = 'get/department/product'

/* ___________ A C T I O N S   ___________ */
export const getProducts = (products) => {
    return {
        type: GET_PRODUCTS_BY_DEPT,
        products
    };
}

/* ___________ T H U N K S   ___________ */
// Get products for department 
export const getProductsThunk = (departmentId) => async(dispatch) => {
    const response = await fetch(`/api/departments/${departmentId}/products`)
    const products = await response.json()
    dispatch(getProducts(products));
};


/* ___________ R E D U C E R ___________ */
const productsReducer = (state = {}, action) => {
    let newState = {};
    switch (action.type) {
        case GET_PRODUCTS_BY_DEPT:
            action.products.forEach(ele => newState[ele.id] = ele)
            return newState


        default:
            return state;
    }
}

export default productsReducer;