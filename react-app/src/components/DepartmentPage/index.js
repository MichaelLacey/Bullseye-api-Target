import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useParams, useHistory } from 'react-router-dom'
import './index.css';
import { getProductsThunk } from "../../store/product";
import { addToCartThunk } from "../../store/cart";
import { getUsersCartThunk } from "../../store/cart";

export default function DepartmentPage() {
    const dispatch = useDispatch();
    const history = useHistory();
    const { departmentId } = useParams();
    const [ loading, setLoading ] = useState(false)

    const productsArr = Object.values(useSelector(state => state.products));
    // Grab user of the session
    const sessionUserObject = Object.values(useSelector(state => state.session))[0];
    const cart = Object.values(useSelector(state => state.cart));
    
    const cartArr = [];
    cart.forEach(ele => cartArr.push(ele.id));
    
    // Have something give some extra time to load all of our images and data
    useEffect(() => {
        setTimeout(() => setLoading(true), 250)
      }, []);

    useEffect(() => {
        dispatch(getProductsThunk(departmentId));
        // If we have a user lets grab that users cart itmes
        if (sessionUserObject?.id) {
            dispatch(getUsersCartThunk());
        }
    }, [dispatch, departmentId]);

if (!productsArr.length) return null;
return (
    <div className="departmentMainDiv">
    {loading &&

        <div className="products">

            {productsArr.map(ele => (
                <div className="productMap" key={`a${ele.id}`}>

                    <Link className="productMapLink" key={`b${ele.id}`} style={{ textDecoration: 'none' }} to={`/departments/${departmentId}/${ele.id}`}>
                        <img key={`c${ele.id}`} className='departmentProductImg' src={`${ele.image_url1}`} alt='spotPic'></img>
                        <h4 className="productsH5" key={`d${ele.id}`}> {ele.name}</h4>
                        <div className="productsArrPrice" key={`e${ele.id}`}>${Number(ele.price).toFixed(2)}</div>
                    </Link>
                    {/* If there is no session user signed it show the same button with a redirect onClick to tell them to log in */}
                    {!sessionUserObject?.id && <button className='deptAddCartBtn' onClick={() => { history.push('/login')}}> Add to cart </button>}
                    {(!cartArr.includes(ele.id) && sessionUserObject?.id) && <button className='deptAddCartBtn' onClick={() => dispatch(addToCartThunk(ele.id))}> Add to cart</button>}
                    {(cartArr.includes(ele.id) && sessionUserObject?.id) && <button className="deptInCartBtn">In cart</button>}
                </div>
            ))}

        </div>
            }
    </div>
)  
}