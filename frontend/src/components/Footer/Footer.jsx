import React from 'react'
import { assets } from '../../assets/assets'
import './Footer.css'

const Footer = () => {
  return (
    <div className='footer' id='footer'>
    <div className='footer-content'>
    <div className='footer-content-left'>
    <img src={assets.logo}  alt='' />
    <p>�� 2021 Food Delivery. All rights reserved.</p>
    <div className='footer-social-icons'>
    <img src={assets.facebook_icon} alt='' />
    <img src={assets.twitter_icon} alt='' />
    <img src={assets.linkedin_icon} alt='' />
    </div>
    </div>
    <div className='footer-content-center'>
    <h2>COMPANY</h2>
    <ul>
        <li>Home</li>
        <li>About Us</li>
        <li>Delivery</li>
        <li>Terms & Conditions</li>
    </ul>
    </div>
    <div className='footer-content-right'>
    <h2>CUSTOMER SUPPORT</h2>
    <ul>
        <li>Contact Us</li>
        <li>FAQ</li>
        <li>Returns & Exchanges</li>
        <li>Privacy Policy</li>
    </ul>
    </div>
    </div>
    <hr />
    <p className='footer-copyright'>Copyright 2024 © FoodoMania. All rights reserved.</p>
    </div>
  )
}

export default Footer