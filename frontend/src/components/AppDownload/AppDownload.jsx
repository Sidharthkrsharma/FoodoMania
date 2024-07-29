import React from 'react'
import { assets } from '../../assets/assets'
import './AppDownload.css'

const AppDownload = () => {
  return (
    <div className='app-download' id='app-download'>
    <p>For better Experience Download <br />Tomato App</p>
    <div className="app-download-platform">
        <img src={assets.play_store} alt="" className="image-hover"/>
        <img src={assets.app_store} alt="" className="image-hover" />
    </div>


    </div>
  )
}

export default AppDownload