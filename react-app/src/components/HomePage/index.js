import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getDepartmentsThunk } from "../../store/department";
import { getProductsThunk } from "../../store/product";
import { getUsersCartThunk } from "../../store/cart";
import { Link } from 'react-router-dom'
import './index.css'
import Slider from "../Carousel";

export default function HomePage() {
    const dispatch = useDispatch();

    const sessionUserObject = Object.values(useSelector(state => state.session))[0];
    const departmentsArr = Object.values(useSelector(state => state.departments));


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
            {/* Carousel Component*/}
            <Slider />

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