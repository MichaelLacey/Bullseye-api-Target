import CategoryDropdown from './CatergoryDropdown';
import React, { useState } from 'react';
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import ProfileDropdown from './ProfileDropdown';
import './navbar.css'

const NavBar = () => {
  const sessionUser = useSelector(state => state.session.user)
  const [openMenu, setOpenMenu] = useState(false);
  const [openMenu2, setOpenMenu2] = useState(false);



  return (
    <nav className='navDiv'>

      <div className="homeButton">
        <NavLink to='/' exact={true} activeClassName='active' id='navLinkLogo' style={{ textDecoration: 'none' }}>
          <i id='homeButton' class="fa-solid fa-bullseye"></i>
        </NavLink>
      </div>


      <div className='categoriesHome'>Bullsye</div>


      <div className="otherNavBtns">
        <div className="categories">
          <h4 onClick={() => setOpenMenu((prev) => !prev)} id='categoryH4'>Categories</h4>
          {openMenu &&
            <CategoryDropdown setOpenMenu={setOpenMenu} openMenu={openMenu} />
          }
        </div>

        {sessionUser && <div id='cartImgDiv'>
          <NavLink to='/cart' exact={true} activeClassName='active' style={{ textDecoration: 'none' }}>
            <img className='cartImg' src='https://i1.wp.com/afriwestmedia.com/wp-content/uploads/2017/03/white-shopping-cart-icon.png?fit=300%2C300' alt='Pic'></img>
          </NavLink>
        </div>}


        <i id="rightsideMenu" class="fa-regular fa-user fa-2x" onClick={() => setOpenMenu2((prev) => !prev)}></i>
        {openMenu2 &&
          <ProfileDropdown setOpenMenu2={setOpenMenu2} openMenu2={openMenu2} />
        }


        {sessionUser && <div id='logout' className='navBtn'>

        </div>}
      </div>

    </nav >
  );
}

export default NavBar;
