import images from '../apis/images';
import axios from 'axios';
import {
  FETCH_IMAGES,
  FETCH_IMAGE,
  FETCH_FLAG
} from './types';

const baseUrl = 'http://127.0.0.1:5000/api/v1.0/';

export const fetchImages = () => async dispatch => {
  const response = await axios.get(`{$baseUrl}/images`);
  dispatch({ type: FETCH_IMAGES, payload: response.data }); 
};

export const fetchImage = id => async dispatch => {
  const response = await images.get(`/images/${id}`);
  dispatch({ type: FETCH_IMAGE, payload: response.data });
  dispatch({ type: FETCH_FLAG, payload: 0});  
};


export const fetchFlag = curFlag =>  dispatch => {
  dispatch({ type: FETCH_FLAG, payload: curFlag });  
};