import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getDepartmentsThunk } from "../../store/department";
import { getProductsThunk } from "../../store/product";
import { getUsersCartThunk } from "../../store/cart";
import { Link } from 'react-router-dom'
import './index.css'

export default function HomePage() {
    const dispatch = useDispatch();

    const sessionUserObject = Object.values(useSelector(state => state.session))[0];
    const departmentsArr = Object.values(useSelector(state => state.departments));
    const products = Object.values(useSelector(state => state.products));


    useEffect(() => {
        dispatch(getProductsThunk(1));
        dispatch(getDepartmentsThunk())
        if (sessionUserObject?.user) {
            dispatch(getUsersCartThunk());
        }
    }, [dispatch]);


    return (
        <div className="homepageMainDiv">
            <h1 id="hpH1"> Hottest Electronics </h1>

            <div className="layer1">

                <div className="product1">
                    <p className="hpProductName">{products[0]?.name}</p>
                    <p className="hpProductName">${products[0]?.price}</p>
                    <Link to={`/departments/${products[0]?.department_id}/${products[0]?.id}`} className="hpImgLink">
                    <img className="hpImg" src={products[0]?.image_url1} alt="" />
                    </Link>
                </div>
                        

                <div className="product2">
                    <p className="hpProductName">{products[5]?.name}</p>
                    <p className="hpProductName">${products[5]?.price}</p>
                    <Link to={`/departments/${products[5]?.department_id}/${products[5]?.id}`} className="hpImgLink">
                    <img className="hpImg" src={products[5]?.image_url1} alt="" />
                    </Link>
                </div>

            </div>

            <div className="layer2">
                <div className="product1">
                    <p className="hpProductName">{products[10]?.name}</p>
                    <p className="hpProductName">${products[10]?.price}</p>
                    <Link to={`/departments/${products[10]?.department_id}/${products[10]?.id}`} className="hpImgLink">
                    <img className="hpImg" src={products[10]?.image_url1} alt="" />
                    </Link>
                </div>

                <div className="product2">
                    
                    <p className="hpProductName">{products[9]?.name}</p>
                    <p className="hpProductName">${products[9]?.price}</p>
                    <Link to={`/departments/${products[9]?.department_id}/${products[9]?.id}`} className="hpImgLink">
                    <img className="hpImg" src={products[9]?.image_url1} alt="" />
                    </Link>
                </div>

            </div>

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