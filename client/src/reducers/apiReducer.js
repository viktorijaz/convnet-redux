import {
  FETCH_IMAGE,
  FETCH_IMAGES
} from '../actions/types';

export const imageReducer = (state = [], action) => {
  if (action.type === FETCH_IMAGES) {
    return [ ...action.payload.images ];
  }
  return state;
};

export const selectedImageReducer = (selectedImage = null, action) => {
  if (action.type === FETCH_IMAGE) {
    return action.payload;
  }
  return selectedImage;
};