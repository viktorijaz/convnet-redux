import images from '../apis/images';
import {
  FETCH_IMAGES,
  FETCH_IMAGE
} from './types';

export const fetchImages = () => async dispatch => {
  const response = await images.get(`/images`);
  dispatch({ type: FETCH_IMAGES, payload: response.data });  
};

export const fetchImage = id => async dispatch => {
  const response = await images.get(`/images/${id}`);
  dispatch({ type: FETCH_IMAGE, payload: response.data });
};