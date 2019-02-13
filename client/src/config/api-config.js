let backendHost;
const apiVersion = 'v1.0';

const hostname = window && window.location && window.location.hostname;

if(hostname === 'localhost') {
  backendHost = 'http://localhost:5000';
} else if(/(aws)|(amazon)/.test(hostname)) {
  backendHost = `http://flask-convnet-env.ufk7cpwipa.eu-central-1.elasticbeanstalk.com`;
} else {
  backendHost = process.env.REACT_APP_BACKEND_HOST || 'http://localhost:8080';
}

export const API_ROOT = `${backendHost}/api/${apiVersion}`;