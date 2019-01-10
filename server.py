#!flask/bin/python
# Based on https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

from flask import Flask, jsonify, abort, request, make_response, url_for, render_template
from flask_cors import CORS
import matplotlib.image as mpimg
import os
import CIFAR10_CNN_Predict_Image
import tensorflow

app = Flask(__name__, template_folder='client/public/' )
CORS(app)

#@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

images = [
    {  'id': 1, 'id_key': 1, 'title': 'No Scrubs', 'duration': '4:05', 'url': 'img\deer.png' },
    { 'id': 2, 'id_key': 2, 'title': 'Macarena', 'duration': '2:30', 'url': 'img/dog.png' },
    { 'id': 3, 'id_key': 3, 'title': 'All Star', 'duration': '3:15', 'url': 'img/truck.png' },
    { 'id': 4, 'id_key': 4, 'title': 'I Want it That Way server', 'duration': '1:45', 'url': 'img/airplane.png' },
    { 'id': 5, 'id_key': 5, 'title': 'I Want it That Way server 5', 'duration': '1:45', 'url': 'img/airplane.png' }
]

def CNN_predict(path):
    """
    Reads the uploaded image file and predicts its label using the saved pre-trained CNN model.
    :return: Either an error if the image is not for CIFAR10 dataset or redirects the browser to a new page to show the prediction result if no error occurred.
    """

    #Reading the image file from the path it was saved in previously.
    img = mpimg.imread(os.path.join(app.root_path, path['url']))

    """
    Checking whether the image dimensions match the CIFAR10 specifications.
    CIFAR10 images are RGB (i.e. they have 3 dimensions). It number of dimenions was not equal to 3, then a message will be returned.
    """
    if(img.ndim) == 3:
        """
        Checking if the number of rows and columns of the read image matched CIFAR10 (32 rows and 32 columns).
        """
        if img.shape[0] == img.shape[1] and img.shape[0] == 32:
            """
            Checking whether the last dimension of the image has just 3 channels (Red, Green, and Blue).
            """
            if img.shape[-1] == 3:
                """
                Passing all conditions above, the image is proved to be of CIFAR10.
                This is why it is passed to the predictor.
                """
                predicted_class = CIFAR10_CNN_Predict_Image.main(img)
                """
                After predicting the class label of the input image, the prediction label is rendered on an HTML page.
                The HTML page is fetched from the /templates directory. The HTML page accepts an input which is the predicted class.
                """
                
                return predicted_class
                #return flask.render_template(template_name_or_list="prediction_result.html", predicted_class=predicted_class)
            #else:
                # If the image dimensions do not match the CIFAR10 specifications, then an HTML page is rendered to show the problem.
                #return flask.render_template(template_name_or_list="error.html", img_shape=img.shape)
        else:
            # If the image dimensions do not match the CIFAR10 specifications, then an HTML page is rendered to show the problem.
            return flask.render_template(template_name_or_list="error.html", img_shape=img.shape)
    return "An error occurred."#Returned if there is a different error other than wrong image dimensions.

def make_public_image(image):
    new_image = {}
    for field in image:
        if field == 'id':
            new_image['uri'] = url_for('get_image', image_id = image['id'], _external = True)
        else:
            new_image[field] = image[field]
    return new_image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v1.0/images', methods = ['GET'])
def get_images():
    return jsonify( { 'images': [*map(make_public_image, images)] } )

@app.route('/api/v1.0/images/<int:image_id>', methods = ['GET'])
def get_image(image_id):
    image = list(filter(lambda t: t['id'] == image_id, images))
    if len(image) == 0:
        abort(404)
    return jsonify( { 'image': CNN_predict(image[0]) } )

if __name__ == '__main__':
    app.run(debug = True)