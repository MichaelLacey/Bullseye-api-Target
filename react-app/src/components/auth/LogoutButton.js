import React from 'react';
import { useDispatch } from 'react-redux';
import { logout } from '../../store/session';
import { useHistory } from 'react-router-dom';
import './index.css'

const LogoutButton = () => {
  const history = useHistory();
  const dispatch = useDispatch();
  const onLogout = async (e) => {
    history.push('/')
    await dispatch(logout());
  };
  // return <button onClick={onLogout} className='navBtn'>Logout</button>;
  return <h4 onClick={onLogout} className='navBtn'>Logout</h4>;
};

export default LogoutButton;
