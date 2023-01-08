
import React from 'react';
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import './navbar.css'

const NavBar = () => {
  const sessionUser = useSelector(state => state.session.user)
  console.log('sessionuser', sessionUser)
  
  return (
    <nav className='navDiv'>

      <div>
        <NavLink to='/' exact={true} activeClassName='active' style={{ textDecoration: 'none' }}>
          <h4 className='navH4'>Home</h4>
        </NavLink>
      </div>
      <div id='cartImgDiv'>
        <NavLink to='/cart' exact={true} activeClassName='active' style={{ textDecoration: 'none' }}>
        <img className='cartImg' src='https://i1.wp.com/afriwestmedia.com/wp-content/uploads/2017/03/white-shopping-cart-icon.png?fit=300%2C300' alt='Pic'></img>
        </NavLink>
      </div>

      { !sessionUser && <div id='loginH4'>
        <NavLink to='/login' exact={true} activeClassName='active' style={{ textDecoration: 'none' }}>
          <h4 className='navH4'>Login</h4>
        </NavLink>
      </div>}

      { !sessionUser && <div>
        <NavLink to='/sign-up' exact={true} activeClassName='active' style={{ textDecoration: 'none' }}>
          <h4 className='navH4'>Sign Up</h4>
        </NavLink>
      </div>}
      

      {sessionUser && <div className='navBtn'>
        <LogoutButton />
      </div>}


    </nav >
  );
}

export default NavBar;
