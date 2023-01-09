import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getDepartmentsThunk } from "../../store/department";
import { getProductsThunk } from "../../store/product";
import { Link } from 'react-router-dom'
import './index.css'

export default function HomePage() {
    const dispatch = useDispatch();

    const departmentsArr = Object.values(useSelector(state => state.departments));
    const products = Object.values(useSelector(state => state.products));
    console.log('products', products)

    useEffect(() => {
        dispatch(getProductsThunk(1));
        dispatch(getDepartmentsThunk())
    }, [dispatch]);


    // <div className="product1">
    //     <div>{products[4]?.name}</div>
    //     <div className="productPriceHP">{products[4]?.price}</div>
    //     <Link className="imgLingHp">
    //         <img className="homepageImg" src={`${products[4]?.image_url1}`} alt='img'></img>
    //     </Link>
    // </div>


    return (
        <div className="homepageMainDiv">

        
            <h1 id="catH2"> Departments </h1>
            <div className="departments">
                {departmentsArr && departmentsArr.map(ele => (
                    <Link className='linkClass' key={`a${ele.id}`} style={{ textDecoration: 'none' }} to={`/departments/${ele.id}`}>
                        <div className="departmentDiv">
                            <img key={ele.id} className='departmentImg' src={`${ele.image_url}`} alt='img'></img>
                            <h4 className="departmentH4" key={`b${ele.id}`}>{ele.name}</h4>
                        </div>
                    </Link>
                ))}

            </div>
        </div>
    )
}