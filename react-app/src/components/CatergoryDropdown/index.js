import React, { useEffect } from 'react';
import { useHistory } from 'react-router-dom'
import './index.css'

export default function CategoryDropdown({ openMenu, setOpenMenu }) {
    const history = useHistory();

    useEffect(() => {
        if (!openMenu) return

        const closeMenu = () => setOpenMenu(false);
        document.addEventListener('click', closeMenu)

    

        return () => document.removeEventListener('click', closeMenu)
    }, [openMenu]);

    return (
        <div className="dropdownMainDiv" >
            <ul className="dropdownUl" >
                <li onClick={() => history.push('/departments/1')}> Electronics </li>
                <li onClick={() => history.push('/departments/2')}> Household Essentials </li>
                <li onClick={() => history.push('/departments/3')}> Sports & Outdoors </li>
                <li onClick={() => history.push('/departments/4')}> Movies & Shows </li>
                <li onClick={() => history.push('/departments/5')}> Personal Care </li>
                <li onClick={() => history.push('/departments/6')}> Kitchen & Dining </li>
            </ul>
        </div>
    )
}