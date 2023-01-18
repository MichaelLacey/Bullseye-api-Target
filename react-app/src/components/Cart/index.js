import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import './index.css'
import { getUsersCartThunk, removeFromCartThunk, checkoutCartThunK  } from "../../store/cart";
import { useHistory } from "react-router-dom";


export default function Cart() {
    const dispatch = useDispatch();
    const history = useHistory();

    const cart = Object.values(useSelector(state => state.cart));

    // Get the sum of every item in the cart
    let sum = 0;
    cart.forEach(ele => sum += ele.price);
    
    let tax = sum * .08;
    let total = sum + tax;
    // Turn all of the variables into numbers that have commas in them
    sum = sum.toLocaleString(undefined, {maximumFractionDigits: 2})
    tax = tax.toLocaleString(undefined, {maximumFractionDigits: 2})
    total = total.toLocaleString(undefined, {maximumFractionDigits: 2})
   
    
    useEffect(() => {
        dispatch(getUsersCartThunk());
    }, [dispatch]);

    const checkout = () => {
        history.push('/cart/order/check-out');
        dispatch(checkoutCartThunK());
    };

    return (
        <div className="mainPageCartDiv">

            <h3>Shopping Cart</h3>
           
            <div className="mainCartDiv">

                <div className="cartDiv">

                    <h4 className="cartSubtotalHeader"> ${`${sum}`} subtotal ● {`${cart.length}`} items</h4>
                    {cart && cart.map(ele => (
                        <div className="cartMapped" key={`${ele.id}`}>

                            <img key={`a${ele.id}`} className='cartProductImg' src={`${ele.image_url1}`} alt='Pic'></img>
                            <h4 key={`b${ele.id}`} className='cartNameH4'>{ele.name}</h4>
                            <h4 className="cartPrice" key={`c${ele.id}`}>${Number(ele.price).toLocaleString(undefined, {maximumFractionDigits: 2})}</h4>
                            <h4 className="deleteProduct" onClick={() => dispatch(removeFromCartThunk(ele.id))} key={`d${ele.id}`}> X </h4>

                        </div>
                    ))}


                </div>

                <div className="orderSummary">
                    <h3 className="summaryTitle">Order summary</h3>

                    <div className="subtotal">
                        <p>Subtotal</p>
                        <p>${`${sum}`}</p>
                    </div>

                    <div className="delivery">
                        <p>Delivery</p>
                        <p className="freeDelivery">Free</p>
                    </div>

                    <div className="tax">
                        <p>Estimated tax</p>
                        <p>${Number(`${tax}`).toFixed(2)}</p>
                    </div>

                    <div className="total">
                        <p>Total</p>
                        <p> ${total}</p>
                    </div>
                        <button className="cartCheckout" onClick={() => checkout()}>Check out</button>
                </div>

            </div>

        </div>
    );
};