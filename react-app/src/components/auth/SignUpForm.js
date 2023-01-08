import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect, Link } from 'react-router-dom';
import { signUp } from '../../store/session';

const SignUpForm = () => {
  const [errors, setErrors] = useState([]);
  const [firstName, setFirstname] = useState('');
  const [lastName, setLastname] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const data = await dispatch(signUp(firstName, lastName, email, password));
      if (data) {
        setErrors(data)
      }
    }
  };

  const updateFirstName = (e) => {
    setFirstname(e.target.value);
  };

  const updateLastName = (e) => {
    setLastname(e.target.value);
  };
  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/' />;
  }

  return (
    <form onSubmit={onSignUp} className='loginForm'>
      <h1 id='loginH1'> Create your Bullseye account </h1>
      <div>
        {errors.map((error, ind) => (
          <div key={ind}>{error}</div>
        ))}
      </div>
      <div className='inputDiv'>
        {/* <label>First Name</label> */}
        <input
        placeholder=' First Name'
          className='inputs'
          type='text'
          name='first_name'
          onChange={updateFirstName}
          value={firstName}
        ></input>
      </div>
      <div className='inputDiv'>
        {/* <label>Last Name</label> */}
        <input
        placeholder=' Last Name'
          className='inputs'
          type='text'
          name='last_name'
          onChange={updateLastName}
          value={lastName}
        ></input>
      </div>
      <div className='inputDiv'>
        {/* <label>Email</label> */}
        <input
        placeholder=' Email'
          className='inputs'
          type='text'
          name='email'
          onChange={updateEmail}
          value={email}
        ></input>
      </div>
      <div className='inputDiv'>
        {/* <label>Password</label> */}
        <input
        placeholder=' Password'
          className='inputs'
          type='password'
          name='password'
          onChange={updatePassword}
          value={password}
        ></input>
      </div>
      <div className='inputDiv'>
        {/* <label>Repeat Password</label> */}
        <input
        placeholder=' Repeat Password'
          className='inputs'
          type='password'
          name='repeat_password'
          onChange={updateRepeatPassword}
          value={repeatPassword}
          required={true}
        ></input>
      </div>
      <button type='submit' id='loginButton'>Sign Up</button>
     <Link to='/login'> <p id='signUpPtag'> Or sign in</p></Link>
    </form>
  );
};

export default SignUpForm;
