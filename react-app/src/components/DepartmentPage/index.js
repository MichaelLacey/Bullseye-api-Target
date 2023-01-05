import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useParams } from 'react-router-dom'
import './index.css';
import { getProductsThunk } from "../../store/product";
import { addToCartThunk } from "../../store/cart";
import { getUsersCartThunk } from "../../store/cart";

export default function DepartmentPage() {
    const dispatch = useDispatch();
    const { departmentId } = useParams();

    const productsArr = Object.values(useSelector(state => state.products));
    // Grab user of the session
    const sessionUserObject = Object.values(useSelector(state => state.session))
    const cart = Object.values(useSelector(state => state.cart));
    
    const cartArr = [];
    cart.forEach(ele => cartArr.push(ele.id))
    
    useEffect(() => {
        dispatch(getProductsThunk(departmentId));
        if (sessionUserObject.user) {
            dispatch(getUsersCartThunk())
        }
    }, [dispatch, departmentId]);


return (
    <div className="departmentMainDiv">

        <div className="products">

            {productsArr.map(ele => (
                <div className="productMap" key={`a${ele.id}`}>

                    <Link className="productMapLink" key={`b${ele.id}`} style={{ textDecoration: 'none' }} to={`/departments/${departmentId}/${ele.id}`}>
                        <img key={`c${ele.id}`} className='departmentProductImg' src={`${ele.image_url1}`} alt='spotPic'></img>
                        <h4 className="productsH5" key={`d${ele.id}`}> {ele.name}</h4>
                        <div className="productsArrPrice" key={`e${ele.id}`}>${Number(ele.price).toFixed(2)}</div>
                    </Link>

                    {!cartArr.includes(ele.id) &&<button className='deptAddCartBtn' onClick={() => dispatch(addToCartThunk(ele.id))}> Add to cart</button>}
                    {cartArr.includes(ele.id) && <button className="deptInCartBtn">In cart</button>}
                </div>
            ))}

        </div>
    </div>
)  
}