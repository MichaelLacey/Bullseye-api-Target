import React, { useEffect } from 'react';
import { useHistory } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux';
import { logout } from '../store/session';
import './navbar.css'

export default function ProfileDropdown({ openMenu2, setOpenMenu2 }) {
    const history = useHistory();
    const dispatch = useDispatch();
    const sessionUser = useSelector(state => state.session.user)

    const onLogout = (e) => {
        history.push('/')
        dispatch(logout());
    };

    useEffect(() => {
        if (!openMenu2) return

        const closeMenu = () => setOpenMenu2(false);
        document.addEventListener('click', closeMenu)



        return () => document.removeEventListener('click', closeMenu)
    }, [openMenu2]);

    return (
        <div className="dropdownMainDiv2" >
            <ul className="dropdownUl2" >
                {!sessionUser && <li onClick={() => history.push('/login')}> Login </li>}
                {!sessionUser && <li onClick={() => history.push('/sign-up')}> Signup </li>}
                {sessionUser && <li onClick={() => onLogout()}> Logout </li>}
                {sessionUser && <li onClick={() => history.push('/cart')}> Cart </li>}
                
            </ul>
        </div>
    )
}