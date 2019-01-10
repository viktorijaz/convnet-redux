import tensorflow as tf
import pickle
import numpy as np
import matplotlib.pyplot as plt
import flask

def main(img):
    """
    The 'main' method accepts an input image array of size 32x32x3 and returns its class label.
    :param sess:TF session created globally.
    :param graph:TF graph of the trained model.
    :param img:RGB image of size 32x32x3.
    :return:Predicted class label.
    """
    #Dataset path containing a binary file with the labels of classes. Useful to decode the prediction code into a significant textual label.
    patches_dir = "..\cifar-10-batches-py\\"
    dataset_array = np.random.rand(1, 32, 32, 3)
    dataset_array[0, :, :, :] = img
    #dataset_array.transpose(0, 3, 2, 1)
    print('img looks like ', img[0:2, 0:4, 0:3])

    """
    Restoring previous created tensors in the training phase based on their given tensor names in the training phase.
    Some of such tensors will be assigned the testing input data and their outcomes (data_tensor, label_tensor, and keep_prop).
    Others are helpful in assessing the model prediction accuracy (softmax_propabilities and softmax_predictions).
    """

    loaded_graph = tf.Graph()
    save_model_path = './model/image_classification'

    with tf.Session(graph=loaded_graph) as sess:
        # Load model
        loader = tf.train.import_meta_graph(save_model_path + '.meta')
        loader.restore(sess, save_model_path)

        # Get Tensors from loaded model
        loaded_x = loaded_graph.get_tensor_by_name('x:0')
        loaded_y = loaded_graph.get_tensor_by_name('y:0')
        loaded_keep_prob = loaded_graph.get_tensor_by_name('keep_prob:0')
        loaded_logits = loaded_graph.get_tensor_by_name('logits:0')
        loaded_acc = loaded_graph.get_tensor_by_name('accuracy:0')

        random_test_features = [img]
        random_test_predictions = sess.run(
            tf.nn.top_k(tf.nn.softmax(loaded_logits), 2),
            feed_dict={
                loaded_x: random_test_features, 
                #loaded_y: random_test_labels, 
                loaded_keep_prob: 1.0
            }
        )

        print('random_test_predictions: ', random_test_predictions)
    
        softmax_propabilities = tf.nn.softmax(loaded_logits, name="softmax_probs")
        softmax_predictions = tf.argmax(loaded_logits, axis=1)

    label_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    return label_names[random_test_predictions.indices[0][0]]
   

