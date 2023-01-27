import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory } from 'react-router-dom'
import { getProductThunk } from "../../store/product";
import { getDepartmentThunk } from "../../store/department";
import './index.css'
import { clearProductAction } from "../../store/department";
import { getUsersCartThunk, addToCartThunk } from "../../store/cart";
import { getProductReviewsThunk } from "../../store/review";

export default function ProductPage() {
    const dispatch = useDispatch();
    const history = useHistory();
    const { productId } = useParams();
    const { departmentId } = useParams();
    const [loading, setLoading] = useState(false)

    const product = Object.values(useSelector(state => state.products))[0];
    const department = Object.values(useSelector(state => state.departments));
    // Grab user of the session
    const sessionUserObject = Object.values(useSelector(state => state.session))[0];
    const cart = Object.values(useSelector(state => state.cart));
    const reviews = Object.values(useSelector(state => state.reviews));
   

    // Find if a user has a review for product then not show the review button
    let reviewBoolean = true
    reviews.forEach(ele => {
        if (sessionUserObject?.id === ele.user_id) {
            reviewBoolean = false
        };
    });

    // Get the avg rating for each product by iterating through reviews  
    // adding the stars up and dividing by the length
    let sum = 0;
    reviews.forEach(ele => sum += ele.rating)
    let avgRating = (sum / reviews.length).toFixed(2)
    const cartArr = [];
    cart.forEach(ele => cartArr.push(ele.id));

    // Have something give some extra time to load all of our images and data
    useEffect(() => {
        setTimeout(() => setLoading(true), 550)
    }, []);

    useEffect(() => {
        if (sessionUserObject?.user) {
            dispatch(getUsersCartThunk());
        }
        dispatch(getProductThunk(productId));
        dispatch(getDepartmentThunk(departmentId));
        dispatch(getProductReviewsThunk(productId));
        return (() => dispatch(clearProductAction()));
    }, [dispatch, productId, departmentId]);

    function reviewNav(ele) {
        history.push(`/edit/review/${ele.id}`, { ele });
    };
    function createReview(product) {
        history.push(`/create/review/${product.id}`, { product });
    };

    if (!product) return null;


    return (
        <div className="productPageMainDiv">
            {loading && 
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
                        <h3>  {reviews.length > 0 ? `Rating ★ ${avgRating}` : 'Be the first to review'} </h3>
                        <h3> Free shipping </h3>
                        <h3> This item isn't sold in stores </h3>
                        {/* If there is no session user signed it show the same button with a redirect onClick to tell them to log in */}
                        {!sessionUserObject?.id && <button className='productAddCartBtn' onClick={() => { history.push('/login') }}> Add to cart </button>}
                        {!cartArr.includes(product.id) && sessionUserObject?.id && <button className='productAddCartBtn' onClick={() => dispatch(addToCartThunk(product.id))}> Add To Cart</button>}
                        {cartArr.includes(product.id) && <button className="productInCartBtn">In cart</button>}

                        {!reviewBoolean &&
                            <button className='productAddCartBtnReview'> Already have review</button>
                        }
                        {reviewBoolean &&
                            <button className='productAddCartBtn' onClick={() => createReview(product)}> Create A Review</button>
                        }
                    </div>

                </div>
            </div>
            }

                {loading && 
            <div className="reviewsMainDiv">
                {reviews && reviews.map(ele => (
                    
                    <div className="review">

                        <h4 id="names"> {ele.first_name} {ele.last_name} </h4>
                        <p id="rating"> ★ {ele.rating} </p>
                        <p id="comment"> {ele.comment} </p>

                        {sessionUserObject?.id === ele.user_id && <button id="edit" onClick={() => reviewNav(ele)}>Edit / Delete</button>}
                    </div>
                ))}
            </div>
            }
        </div>

    );
};