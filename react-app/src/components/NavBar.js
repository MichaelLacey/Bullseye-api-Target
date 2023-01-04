
import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import './navbar.css'

const NavBar = () => {
  return (
    <nav className='navDiv'>

      <div>
        <NavLink to='/' exact={true} activeClassName='active' style={{ textDecoration: 'none' }}>
          <h4 className='navH4'>Home</h4>
        </NavLink>
      </div>

      <div>
        <NavLink to='/login' exact={true} activeClassName='active' style={{ textDecoration: 'none' }}>
          <h4 className='navH4'>Login</h4>
        </NavLink>
      </div>

      <div>
        <NavLink to='/sign-up' exact={true} activeClassName='active' style={{ textDecoration: 'none' }}>
          <h4 className='navH4'>Sign Up</h4>
        </NavLink>
      </div>

      {/* <div>
        <NavLink to='/users' exact={true} activeClassName='active' style={{ textDecoration: 'none' }}>
          <h4 className='navH4'>Users</h4>
        </NavLink>
      </div> */}
      
      <div>
        <NavLink to='/cart' exact={true} activeClassName='active' style={{ textDecoration: 'none' }}>
        <img className='cartImg' src='https://i1.wp.com/afriwestmedia.com/wp-content/uploads/2017/03/white-shopping-cart-icon.png?fit=300%2C300' alt='Pic'></img>
        </NavLink>
      </div>

      <div className='navBtn'>
        <LogoutButton />
      </div>


    </nav >
  );
}

export default NavBar;
