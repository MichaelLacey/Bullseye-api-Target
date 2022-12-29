
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

      <div>
        <NavLink to='/users' exact={true} activeClassName='active' style={{ textDecoration: 'none' }}>
          <h4 className='navH4'>Users</h4>
        </NavLink>
      </div>

      <div className='navBtn'>
        <LogoutButton />
      </div>


    </nav >
  );
}

export default NavBar;
