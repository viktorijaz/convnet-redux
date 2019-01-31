#!flask/bin/python
# Based on https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

from flask import Flask, jsonify, abort, request, make_response, url_for, render_template
from flask_cors import CORS
import matplotlib.image as mpimg
import os
import CIFAR10_CNN_Predict_Image
import tensorflow
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__, )

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class FileContents(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(300))
    data = db.Column(db.LargeBinary)

class FileContentsSchema(ma.Schema):
    class Meta:
        model = FileContents
        #fields = ('id', 'name', 'data')

file_schema = FileContentsSchema()
files_schema = FileContentsSchema(many=True)

# endpoint to show all images
@app.route("/api/v1.0/images2", methods=["GET"])
def get_images2():
    all_images = FileContents.query.all()
    result = files_schema.dump(all_images)
    return jsonify(result.data)


#@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

images = [
    {  'id': 1, 'id_key': 1, 'title': 'Airplane', 'url': 'img/airplane.png' },
    {  'id': 2, 'id_key': 2, 'title': 'Airplane', 'url': 'img/airplane-1.png' },
    {  'id': 3, 'id_key': 3, 'title': 'Airplane', 'url': 'img/airplane-2.png' },
    {  'id': 4, 'id_key': 4, 'title': 'Automobile', 'url': 'img/automobile.png' },
    {  'id': 5, 'id_key': 5, 'title': 'Automobile', 'url': 'img/automobile-1.png' },
    {  'id': 6, 'id_key': 6, 'title': 'Automobile', 'url': 'img/automobile-2.png' },
    {  'id': 7, 'id_key': 7, 'title': 'Bird', 'url': 'img/bird.png' },
    {  'id': 8, 'id_key': 8, 'title': 'Bird', 'url': 'img/bird-1.png' },
    {  'id': 9, 'id_key': 9, 'title': 'Bird', 'url': 'img/bird-2.png' },
    {  'id': 10, 'id_key': 10, 'title': 'Cat', 'url': 'img/cat.png' },
    {  'id': 11, 'id_key': 11, 'title': 'Cat', 'url': 'img/cat-1.png' },
    {  'id': 12, 'id_key': 12, 'title': 'Cat', 'url': 'img/cat-2.png' },
    {  'id': 13, 'id_key': 13, 'title': 'Deer', 'url': 'img/deer.png' },
    {  'id': 14, 'id_key': 14, 'title': 'Deer', 'url': 'img/deer-1.png' },
    {  'id': 15, 'id_key': 15, 'title': 'Deer', 'url': 'img/deer-2.png' },
    {  'id': 16, 'id_key': 16, 'title': 'Dog', 'url': 'img/dog.png' },
    {  'id': 17, 'id_key': 17, 'title': 'Dog', 'url': 'img/dog-1.png' },
    {  'id': 18, 'id_key': 18, 'title': 'Dog', 'url': 'img/dog-2.png' },
    {  'id': 19, 'id_key': 19, 'title': 'Frog', 'url': 'img/frog.png' },
    {  'id': 20, 'id_key': 20, 'title': 'Frog', 'url': 'img/frog-1.png' },
    {  'id': 21, 'id_key': 21, 'title': 'Frog', 'url': 'img/frog-2.png' },
    {  'id': 22, 'id_key': 22, 'title': 'Horse', 'url': 'img/horse.png' },
    {  'id': 23, 'id_key': 23, 'title': 'Horse', 'url': 'img/horse-1.png' },
    {  'id': 24, 'id_key': 24, 'title': 'Horse', 'url': 'img/horse-2.png' },
    {  'id': 25, 'id_key': 25, 'title': 'Ship', 'url': 'img/ship.png' },
    {  'id': 26, 'id_key': 26, 'title': 'Ship', 'url': 'img/ship-1.png' },
    {  'id': 27, 'id_key': 27, 'title': 'Ship', 'url': 'img/ship-2.png' },
    {  'id': 28, 'id_key': 28, 'title': 'Truck', 'url': 'img/truck.png' },
    {  'id': 29, 'id_key': 29, 'title': 'Truck', 'url': 'img/truck-1.png' },
    {  'id': 30, 'id_key': 30, 'title': 'Truck', 'url': 'img/truck-2.png' }
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

@app.route('/form')
def upload():
   return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def handle():
   file =  request.files['inputFile']

   newFile = FileContents(name=file.filename, data=file.read())
   db.session.add(newFile)
   db.session.commit()

   return 'Saved ' + file.filename + ' to the database'


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