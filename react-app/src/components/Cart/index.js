import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useParams } from 'react-router-dom'
import './index.css'
import { getUsersCartThunk } from "../../store/cart";

export default function Cart() {
    const dispatch = useDispatch();

    const cart = Object.values(useSelector(state => state.cart));
    console.log('Cart', cart)
    let sum = 0;
    cart.forEach(ele => {
        sum += ele.price
    });
    let tax = sum * .08
    let sumStr = sum.toString()
    let sumArr = sumStr.split('')
    // Add a comma in the number for subtotal! 
    if (sumArr.length) {

        if (sumArr.length > 5) {
            sumArr.splice(1, 0, ',')
            console.log('sum', sumArr.join(''))
            sumArr = sumArr.join('')
        }

        // implent another if statement for purchases over 10k
        
    }
    let total = sum + tax
    let totalStr = total.toFixed(2).toString()
    let totalArr = totalStr.split('')
    // Add a comma in the number for total! 
    if (total > 1000) {

        if (totalArr.length > 5) {
            totalArr.splice(1, 0, ',')
            console.log('total', totalArr.join(''))
            totalArr = totalArr.join('')
        }

        // implent another if statement for purchases over 10k
        
    }
    
    useEffect(() => {
        dispatch(getUsersCartThunk())
    }, [dispatch]);

    return (
        <div className="mainPageCartDiv">

            <h3>Shopping Cart</h3>
            {/* <h4> $100 subtotal ● 5 items</h4> */}

            <div className="mainCartDiv">

                <div className="cartDiv">

                    <h4 className="cartSubtotalHeader"> ${`${sumArr}`} subtotal ● {`${cart.length}`} items</h4>
                    {cart && cart.map(ele => (
                        <div className="cartMapped">

                            <img key={`a${ele.id}`} className='cartProductImg' src={`${ele.image_url1}`} alt='Pic'></img>
                            <h4 key={`b${ele.id}`} className='cartNameH4'>{ele.name}</h4>
                            <h4 className="cartPrice">${`${ele.price}`}</h4>
                            <h4 className="deleteProduct"> X </h4>

                        </div>
                    ))}


                </div>

                <div className="orderSummary">
                    <h3 className="summaryTitle">Order summary</h3>

                    <div className="subtotal">
                        <p>Subtotal</p>
                        <p>${`${sumArr}`}</p>
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
                        <p> ${`${totalArr}`}</p>
                    </div>
                        <button className="cartCheckout">Check out</button>
                </div>

            </div>

        </div>
    );
};