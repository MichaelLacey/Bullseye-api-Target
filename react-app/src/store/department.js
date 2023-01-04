const GET_DEPARTMENTS = 'get/departments'
const GET_DEPARTMENT = 'get/department'
const CLEARPRODUCT = 'spot/clearProduct'
/* ___________ A C T I O N S   ___________ */

export const getDepartments = (departments) => {
    return {
        type: GET_DEPARTMENTS,
        departments
    };
};

export const getDepartment = (department) => {
    return {
        type: GET_DEPARTMENT,
        department
    };
};
// Clear state or empty it in the return of a useeffect so its empty upon leaving the component
export const clearProductAction = () => {
    return {
      type: CLEARPRODUCT,
    };
  };


/* ___________ T H U N K S   ___________ */

// Get all departments
export const getDepartmentsThunk = () => async (dispatch) => {
    const response = await fetch('/api/departments');
    const departments = await response.json();
    dispatch(getDepartments(departments));
};

// Get one department
export const getDepartmentThunk = (departmentId) => async(dispatch) => {
    const response = await fetch(`/api/departments/${departmentId}`);
    const department = await response.json();
    dispatch(getDepartment(department));
};

/* ___________ R E D U C E R ___________ */
const departmentsReducer = (state = {}, action) => {
    let newState = {};
    switch (action.type) {

        case CLEARPRODUCT:
            return newState

        case GET_DEPARTMENTS:
            action.departments.forEach(ele => newState[ele.id] = ele)
            return newState

        case GET_DEPARTMENT:
            newState = { ...action.department }
            return newState
            
        default:
            return state;
            
    };
};

export default departmentsReducer;