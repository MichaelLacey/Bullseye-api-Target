import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from 'react-router-dom'
import { getProductThunk } from "../../store/product";
import { getDepartmentThunk } from "../../store/department";
import './index.css'
import { clearProductAction } from "../../store/department";
import { getUsersCartThunk, addToCartThunk } from "../../store/cart";

export default function ProductPage() {
    const dispatch = useDispatch();
    const { productId } = useParams();
    const { departmentId } = useParams();


    const product = Object.values(useSelector(state => state.products))[0]
    const department = Object.values(useSelector(state => state.departments))
    // Grab user of the session
    const sessionUserObject = Object.values(useSelector(state => state.session))
    const cart = Object.values(useSelector(state => state.cart));
    
    const cartArr = [];
    cart.forEach(ele => cartArr.push(ele.id))

    useEffect(() => {
        dispatch(getProductThunk(productId))
        dispatch(getDepartmentThunk(departmentId))

        if (sessionUserObject.user) {
            dispatch(getUsersCartThunk())
        }
        return (() => dispatch(clearProductAction()))
    }, [dispatch, productId, departmentId]);

    if (!product) return null

    return (
        <div className="productPageMainDiv">

            <div className="proudctsPageMapped">
                <div className="departmentAndProductName">
                    <h5>Bullsye/{`${department[2]}`}</h5>
                    <h1>{product.name}</h1>
                </div>

                <div className="productDiv">
                    <div className="productImages">
                        <img className='productImgLeft' src={`${product.image_url2}`} alt='productimg'></img>
                        <img className='productImgLeft' src={`${product.image_url3}`} alt='productimg'></img>
                        <img className='productImgLeft' src={`${product.image_url4}`} alt='productimg'></img>
                    </div>

                    <div className="mainImage">
                        <img className='productImg' src={`${product.image_url1}`} alt='productimg'></img>
                    </div>

                    <div className="priceAndRightMenu">
                        <h2>$ {Number(product.price).toFixed(2)}</h2>
                        <h3> Rating ★ </h3>
                        <h3> Free shipping </h3>
                        <h3> This item isn't sold in stores </h3>
                        {!cartArr.includes(product.id) &&<button className='productAddCartBtn' onClick={() => dispatch(addToCartThunk(product.id))}> Add to cart</button>}
                        {cartArr.includes(product.id) && <button className="productInCartBtn">In cart</button>}
                    </div>

                </div>
            </div>
        </div>
    )
}