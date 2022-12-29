
const GET_DEPARTMENTS = 'get/departments'

/* ___________ A C T I O N S   ___________ */

export const getDepartments = (departments) => {
    return {
        type: GET_DEPARTMENTS,
        departments
    };
};



/* ___________ T H U N K S   ___________ */

// Get all departments
export const getDepartmentsThunk = () => async (dispatch) => {
    const response = await fetch('/api/departments');
    const departments = await response.json();
    console.log('departments', departments)
    dispatch(getDepartments(departments))
}


/* ___________ R E D U C E R ___________ */
const departmentsReducer = (state = {}, action) => {
    let newState = {};
    switch (action.type) {
        case GET_DEPARTMENTS:
            action.departments.forEach(ele => newState[ele.id] = ele)
            return newState


        default:
            return state;
    }
}

export default departmentsReducer;