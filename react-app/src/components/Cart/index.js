import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useParams } from 'react-router-dom'
import './index.css'
import { getUsersCartThunk } from "../../store/cart";

export default function Cart() {
    const dispatch = useDispatch();

    const cart = Object.values(useSelector(state => state.cart));
    console.log('Cart', cart)

    useEffect(() => {
        dispatch(getUsersCartThunk())
    }, [dispatch]);
    
    return (
        <div className="cartDiv">

            <div> Hello cart page</div>
            {cart && cart.map(ele => (

                <div className="cartMapped">

                    <img key={`a${ele.id}`} className='cartProductImg' src={`${ele.image_url1}`} alt='Pic'></img>
                    <h4 key={`b${ele.id}`}>{ele.name}</h4>

                </div>

            ))}

        </div>
    );
};