import React from 'react';
import ImageList from './ImageList';
import ImageDetail from './ImageDetail';

const App = () => {
  return (
    <div className="d-flex justify-content-center">
        <div className="col-md-6 p-0 box-shadow">
          <div className="card card-h">
            <div className="card-header">
              Choose from a l ist of images
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