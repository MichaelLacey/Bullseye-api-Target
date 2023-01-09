import './index.css';
import { useEffect, useState } from 'react';
import { useParams, useHistory, useLocation } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { getOneReviewThunk } from '../../store/review';
import { getProductThunk } from '../../store/product';
import { editReviewThunk } from '../../store/review';
import { deleteReviewThunk } from '../../store/review';

export default function EditReview() {
    const dispatch = useDispatch();
    const history = useHistory();
    const { reviewId } = useParams();
    // Use location from history.push from ProductPage component
    // like passing props or using react context
    const location = useLocation()
    const data = location.state.ele;


    // Grab user of the session
    let sessionUserId = useSelector(state => state.session.user.id);
    const review = Object.values(useSelector(state => state.reviews));
    const product = Object.values(useSelector(state => state.products));
    let [comment, setComment] = useState('' || data.comment);
    let [rating, setRating] = useState(1 || data.rating);
    const [validationErrors, setValidationErrors] = useState([]);
    const productId = review[2]

    useEffect(() => {
        dispatch(getOneReviewThunk(reviewId))
        dispatch(getProductThunk(productId));
        setValidationErrors(validationErrors);
    }, [productId]);

    const deleteReview = (reviewId) => {
        {
            if (window.confirm('Are you sure you want to delete this review? This action cannt be undone.')) {
                { dispatch(deleteReviewThunk(reviewId)) }
            }
            history.push('/')
        }
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        const review = {
            rating,
            comment,

        };


        setComment('');
        setRating(1);
        let reviewDispatch = dispatch(editReviewThunk(review, parseInt(reviewId)));

        if (reviewDispatch) {
            history.push(`/`)
        };
    };
    if (!review || !product.length) return null
    return (
        <form className='editReviewForm' onSubmit={handleSubmit}>
            <div className="imgDiv">
                <img className='editproductImg' src={`${product[0].image_url1}`} alt='productimg'></img>
            </div>
            <div className="formDiv">
                <h className='reviewH2'>Edit your review for : </h>
                <h5>{product[0].name}</h5>
                <h5>Write out your review</h5>
                <ul className='createReviewErrors'>
                    {validationErrors.map((error, idx) => (
                        <li key={idx}>{error}</li>
                    ))}
                </ul>
                <label>
                    <textarea
                        className='reviewTextArea'
                        placeholder='Write a review'
                        type="text"
                        value={comment}
                        onChange={(e) => setComment(e.target.value)}
                        required
                    />
                </label>
                <label>
                    <h5 id='starRating'> How many stars would you rate this product ?</h5>
                    <select
                        className='starsSelect'
                        onChange={(e) => setRating(e.target.value)}
                        value={rating}
                        required
                    >
                        <option value={1}>1</option>
                        <option value={2}>2</option>
                        <option value={3}>3</option>
                        <option value={4}>4</option>
                        <option value={5}>5</option>
                    </select>
                </label>
                <button type='submit' className='editReviewButton' disabled={validationErrors.length > 0} > Submit  </button>
                <button className='deleteReviewButton' onClick={() => deleteReview(reviewId)}> Delete  </button>
            </div>
        </form>

    );
};