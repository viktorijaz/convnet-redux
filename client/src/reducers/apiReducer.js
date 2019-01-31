import {
  FETCH_IMAGE,
  FETCH_IMAGES,
  FETCH_FLAG
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

export const fetchFlagReducer = (initFlag = 0, action) => {
  if (action.type === FETCH_FLAG) {
    return action.payload;
  }
  return initFlag;
};