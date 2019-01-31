import React from 'react';
import ImageList from './ImageList';
import ImageDetail from './ImageDetail';

const App = () => {
  return (
    <div className="d-flex justify-content-center">
        <div className="col-md-6 p-0">
          <div className="card card-h box-shadow mb-3">
            <div className="card-header bottomed">
              <i className="fa fa fa-id-card fa-lg color-2"  aria-hidden="true"></i>
              Project Info
            </div>
            <div className="card-body p-4 flex-md-row">
              <p>Using convolutional Neural Networks for image classification.</p>
              <p>The model used is pre-trained. The front-end is built with <strong>React/Redux</strong> and back-end with python <strong>Flask</strong> framework</p>
            </div>
          </div>
          <div className="card card-h box-shadow">
            <div className="card-header bottomed">
              <i className="fa fa-camera-retro fa-lg color-1"></i> Choose from a list of images
            </div>
            <div className="card-body p-4 flex-md-row">
              <ImageList />
            </div>
            </div>
        </div>
        <div className="col-md-6 p-0  pulled-down">
            <ImageDetail />
        </div>
     </div>
  );
};

export default App;