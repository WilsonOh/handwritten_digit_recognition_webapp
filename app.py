from flask import Flask, request
from neural_network.Network import Network
import numpy as np
import requests
import json
import os


path_to_static = os.path.abspath("./static")
app = Flask(__name__, static_folder=path_to_static, static_url_path="/")

weights = np.load('./neural_network/weights.npy', allow_pickle=True)
biases = np.load('./neural_network/biases.npy', allow_pickle=True)
net = Network([784, 30, 10], weights=weights, biases=biases)


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/submit", methods=['POST'])
def submit():
    grid = request.get_json()
    formatted_req = {
        "instances": grid
    }
    r = requests.post(
        "http://13.215.15.247:8501/v1/models/digit_recognition/versions/0:predict", data=json.dumps(formatted_req))
    prediction = r.json()
    print(prediction)
    digit = np.argmax(*prediction['predictions'])
    return str(digit)


# Version using local neural network
# @app.route("/submit", methods=['POST'])
# def submit():
#     grid = request.get_json()
#     digit = net.show_num(np.array(grid).reshape(784, 1))
#     return str(digit)
