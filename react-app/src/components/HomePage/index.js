import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getDepartmentsThunk } from "../../store/department";
import { Link } from 'react-router-dom'
import './index.css'

export default function HomePage() {
    const dispatch = useDispatch();

    const departmentsArr = Object.values(useSelector(state => state.departments));

    useEffect(() => {
        dispatch(getDepartmentsThunk())
    }, [dispatch]);

    return (
        <div className="homepageMainDiv">

            <div className="departments">
                {departmentsArr.map(ele => (
                    <Link className='linkClass' key={`a${ele.id}`} style={{ textDecoration: 'none' }} to={`/departments/${ele.id}`}>
                    <div className="departmentDiv">
                        <img key={ele.id} className='departmentImg' src={`${ele.image_url}`} alt='spotPic'></img>
                        <h4 className="departmentH4">{ele.name}</h4>
                    </div>
                    </Link>
                ))}

            </div>
        </div>
    )
}