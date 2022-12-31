import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link, useParams } from 'react-router-dom'
import './index.css'
import { getProductsThunk } from "../../store/product";

export default function DepartmentPage() {
    const dispatch = useDispatch();
    const { departmentId } = useParams();
    
    // This is working now just map it when you get on next!!!!!!
    const productsArr = Object.values(useSelector(state => state.products))
    console.log('Products by department !!!!!', productsArr);

    useEffect(() => {
        dispatch(getProductsThunk(departmentId))
    }, [dispatch, departmentId]);


    return (
        <div className="departmentMainDiv">

            <div className="products">

                {productsArr.map(ele => (
                    <div className="productMap">
                    <Link>
                        <div>{ele.name}</div>
                        <img key={ele.id} className='departmentProductImg' src={`${ele.image_url}`} alt='spotPic'></img>
                    </Link>
                </div>
                    ))}

            </div>
        </div>
    )
}