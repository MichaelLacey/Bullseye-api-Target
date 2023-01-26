import { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import './index.css'
import { NavLink } from 'react-router-dom';
import { getProductsThunk } from "../../store/product";


export default function Slider() {
  const dispatch = useDispatch()
  const [currentIndex, setCurrentIndex] = useState(0);
  const products = Object.values(useSelector(state => state.products));

  // Get the products from department 1 (electronics)
  useEffect(() => {
    dispatch(getProductsThunk(1))
  }, [dispatch])



  function handlePrevious() {
    setCurrentIndex(currentIndex - 1);
    if (currentIndex === 0) {
        setCurrentIndex(products.length-1)
    }
  }

  function handleNext() {
    setCurrentIndex(currentIndex + 1)
    if (currentIndex === products.length-1) {
        setCurrentIndex(0)
    }
  }

  if (!products) {
    return null
  }

return (
    <>
    <div className='allCarousel'>
      <button className='arrow-button-left' onClick={handlePrevious}></button>
      <NavLink to={`/departments/${products[currentIndex]?.department_id}/${products[currentIndex]?.id}`}>
      <img
      className='sliderImages'
      src={products[currentIndex]?.image_url1}
      alt="description for screen readers"
      onError={e => { e.currentTarget.src ="https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930"; }}
    />
      </NavLink>
      <button className='arrow-button-right' onClick={handleNext}></button>
    </div>
    </>

)
}