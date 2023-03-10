import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import NavBar from './components/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import User from './components/User';
import { authenticate } from './store/session';
import './index.css'
import HomePage from './components/HomePage';
import DepartmentPage from './components/DepartmentPage';
import ProductPage from './components/ProductPage';
import Cart from './components/Cart';
import EditReview from './components/EditReview';
import CreateReview from './components/CreateReview';
import CheckOut from './components/CheckOut';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar />
      <Switch>
        <Route path='/login' exact={true}>
          <LoginForm />
        </Route>
        <Route path='/sign-up' exact={true}>
          <SignUpForm />
        </Route>
        <ProtectedRoute path='/users' exact={true} >
          <UsersList />
        </ProtectedRoute>
        <ProtectedRoute path='/users/:userId' exact={true} >
          <User />
        </ProtectedRoute>
        <Route path='/' exact={true} >
          <HomePage />
        </Route>
        <Route path='/departments/:departmentId' exact={true}>
          <DepartmentPage />
        </Route>
        <Route path='/departments/:departmentId/:productId' exact={true}>
          <ProductPage />
        </Route>
        <ProtectedRoute path='/cart' exact={true} >
          <Cart />
        </ProtectedRoute>
        <ProtectedRoute path='/edit/review/:reviewId' exact={true} >
          <EditReview />
        </ProtectedRoute>
        <ProtectedRoute path='/create/review/:productId' exact={true} >
          <CreateReview />
        </ProtectedRoute>
        <ProtectedRoute path='/cart/order/check-out' exact={true} >
          <CheckOut />
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
