import { combineReducers } from 'redux';
import { imageReducer, selectedImageReducer } from './apiReducer';

export default combineReducers({
  selectedImage: selectedImageReducer,
  images: imageReducer
});
  