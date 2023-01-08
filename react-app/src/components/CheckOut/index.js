import React from "react";

import './index.css'

export default function CheckOut() {



    return (
        <div className="checkoutMainDiv">
            <div id="imgDiv">
                <img className='productImgLeft' id="checkoutImg" src='https://ih1.redbubble.net/image.3436365321.5674/st,small,507x507-pad,600x600,f8f8f8.jpg' alt='productimg'></img>
            </div>
            <div className="otherDiv">
                <h2> Thanks for shopping at Bullseye ! </h2>
                <p> Please check your email for confirmation </p>
                <p> Your order will be ready for pickup in 60 minutes </p>
                <p> Please proceed to the pickup line to retrieve your order when you arrive </p>
                <p> 555 App Academy Avenue, San Francisco, CA 94108 </p>
            </div>
        </div>
    );
};