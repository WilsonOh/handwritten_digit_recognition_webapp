# Quite a messy collection of things related to handwritten digit recognition

## k_nearest_neighbour 
contains:
* algorithm for predicting a handwritten digit based on the K nearest neigbour algorithm
* input files consisting of the mnist dataset parsed

## neural_network
contains:
* a neural network class adapted from [Michael Nielsen's website](http://neuralnetworksanddeeplearning.com/)
* useful helper functions defined in their respective files
* pre-trained weights and biases in the form of numpy object files

## static
contains:
* html, css and javascript files that make up the webapp

## To run the webapp
### Python
Requirements:
* numpy
* requests
* flask

To run the flask app, simply enter `flask run`
### Node
Requirements
* expressjs
* node-fetch

To run the node app, simply enter `node server.js`
