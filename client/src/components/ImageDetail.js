import React from 'react';
import { connect } from 'react-redux';
import { fetchFlag } from '../actions';

const ImageDetail = ({ image, flag }) => {
  let header;
  let main = '';
  let flagDiv = '';
  let flagstate = {flag: false};

  if (!image) {
    header = <div>Select an image</div>;
  } else {
    header = <div></div>;
    main = <div>
        <p>The class for this image is: </p><h1>{image.image}</h1></div>;
  }

  return (
    <div className="card bg-blue card-h text-wh text-center">
      <div className="card-header">{header}</div>
      <div className="card-body">
          <div style={{display: flag? 'block' : 'none' }} >
            <div className="loader">
              <img src="img/loader.gif" />
             </div>
          </div>
          <div style={{display: !flag? 'block' : 'none' }} >
          {main}
          </div>
      </div>
    </div>
  );
};

const mapStateToProps = state => {
  return { 
    image: state.selectedImage,
    flag: state.flag 
  };
};

export default connect(mapStateToProps, 
  { fetchFlag }
  )(ImageDetail);