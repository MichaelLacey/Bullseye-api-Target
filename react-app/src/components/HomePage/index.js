import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getDepartmentsThunk } from "../../store/department";
import './index.css'

export default function HomePage() {
    const dispatch = useDispatch();

    const departmentsArr = Object.values(useSelector(state => state.departments))

    useEffect(() => {
        dispatch(getDepartmentsThunk())
    }, [dispatch])

    return (
        <div className="homepageMainDiv">
            <div className="departments">

                {departmentsArr.map(ele => (
                    <div className="departmentDiv">
                        <h4 className="departmentH4">{ele.name}</h4>
                        <img key={ele.id} className='departmentImg' src={`${ele.image_url}`} alt='spotPic'></img>
                    </div>
                ))}

            </div>
        </div>
    )
}