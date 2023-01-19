
import React from 'react';
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import './navbar.css'

const NavBar = () => {
  const sessionUser = useSelector(state => state.session.user)

  return (
    <nav className='navDiv'>

      <div className="homeButton">
        <NavLink to='/' exact={true} activeClassName='active' id='navLinkLogo' style={{ textDecoration: 'none' }}>
          <i id='homeButton' class="fa-solid fa-bullseye"></i>
        </NavLink>
      </div>

      <div className="otherNavBtns">

        <div>
          <NavLink to='/' exact={true} activeClassName='active' style={{ textDecoration: 'none' }}>
            <h4 className='navH4'>Home</h4>
          </NavLink>
        </div>

        {sessionUser && <div id='cartImgDiv'>
          <NavLink to='/cart' exact={true} activeClassName='active' style={{ textDecoration: 'none' }}>
            <img className='cartImg' src='https://i1.wp.com/afriwestmedia.com/wp-content/uploads/2017/03/white-shopping-cart-icon.png?fit=300%2C300' alt='Pic'></img>
          </NavLink>
        </div>}

        {!sessionUser && <div id='loginH4'>
          <NavLink to='/login' exact={true} activeClassName='active' style={{ textDecoration: 'none' }}>
            <h4 className='navH4'>Login</h4>
          </NavLink>
        </div>}

        {!sessionUser && <div>
          <NavLink to='/sign-up' exact={true} activeClassName='active' style={{ textDecoration: 'none' }}>
            <h4 className='navH4'>Sign Up</h4>
          </NavLink>
        </div>}


        {sessionUser && <div id='logout' className='navBtn'>
          <LogoutButton />
        </div>}
      </div>

    </nav >
  );
}

export default NavBar;
