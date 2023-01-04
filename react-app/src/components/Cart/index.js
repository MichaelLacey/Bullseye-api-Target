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
        <div className="mainPageCartDiv">

            <h3>Shopping Cart</h3>
            {/* <h4> $100 subtotal ● 5 items</h4> */}

            <div className="mainCartDiv">

                <div className="cartDiv">

                    <h4> $100 subtotal ● 5 items</h4>
                    {cart && cart.map(ele => (
                        <div className="cartMapped">


                            <img key={`a${ele.id}`} className='cartProductImg' src={`${ele.image_url1}`} alt='Pic'></img>
                            <h4 key={`b${ele.id}`}>{ele.name}</h4>
                            <h4 className="cartPrice">${`${ele.price}`}</h4>

                        </div>
                    ))}


                </div>

                <div className="orderSummary">
                    <h3 className="summaryTitle">Order summary</h3>

                    <div className="subtotal">
                        <p >Subtotal</p>
                        <p>money amount</p>
                    </div>

                    <div className="delivery">
                        <p>delivery</p>
                        <p className="freeDelivery">Free</p>
                    </div>

                    <div className="tax">
                        <p>Estimated tax</p>
                        <p>money amount</p>
                    </div>

                    <div className="total">
                        <p>Total</p>
                        <p> $Amount</p>
                    </div>
                    
                </div>

            </div>

        </div>
    );
};