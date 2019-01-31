import { combineReducers } from 'redux';
import { imageReducer, selectedImageReducer, fetchFlagReducer } from './apiReducer';

export default combineReducers({
  selectedImage: selectedImageReducer,
  images: imageReducer,
  flag: fetchFlagReducer
});
  