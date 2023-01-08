import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect, useHistory } from 'react-router-dom';
import { login } from '../../store/session';

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  const history = useHistory();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/' />;
  }

  return (
    <form className='loginForm' onSubmit={onLogin}>
        <h1 id='loginH1'> Sign into your Bullseye account </h1>
      <div>
        {errors.map((error, ind) => (
          <div key={ind}>{error}</div>
        ))}
      </div>
      <div className='inputDiv'>
        {/* <label htmlFor='email'>Email</label> */}
        <input
          className='inputs'
          name='email'
          type='email'
          placeholder='Email'
          value={email}
          onChange={updateEmail}
        />
      </div>
      <div className='inputDiv'>
        {/* <label htmlFor='password'>Password</label> */}
        <input
          className='inputs'
          name='password'
          type='password'
          placeholder='Password'
          value={password}
          onChange={updatePassword}
        />
      </div>
      <button type='submit' id='loginButton'>Login</button>
      <button type='submit' id='loginButton' onClick={() => { setEmail('demo@aa.io'); setPassword('password')}}> Demo User </button>
      <button type='submit' id='linkToSignup' onClick={() => {history.push('/sign-up')}}> Create Your Bullseye Account </button>
    </form>
  );
};

export default LoginForm;
