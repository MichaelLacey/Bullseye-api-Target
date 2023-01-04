import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useParams } from 'react-router-dom'
import './index.css'
import { getProductsThunk } from "../../store/product";

export default function DepartmentPage() {
    const dispatch = useDispatch();
    const { departmentId } = useParams();

    const productsArr = Object.values(useSelector(state => state.products))

    useEffect(() => {
        dispatch(getProductsThunk(departmentId))
    }, [dispatch, departmentId]);


    return (
        <div className="departmentMainDiv">

            <div className="products">

                {productsArr.map(ele => (
                    <div className="productMap">

                        <Link className="productMapLink" key={`a${ele.id}`} style={{ textDecoration: 'none' }} to={`/departments/${departmentId}/${ele.id}`}>
                            <img key={ele.id} className='departmentProductImg' src={`${ele.image_url1}`} alt='spotPic'></img>
                            <h4 className="productsH5">{ele.name}</h4>
                            <div className="productsArrPrice">${Number(ele.price).toFixed(2)}</div>
                            <h4 className="avgStarRatingpa"> ★0.0 </h4>
                        </Link>
                        
                        <button className='deptAddCartBtn'> Add to cart</button>
                    </div>
                ))}

            </div>
        </div>
    )
}