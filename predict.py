import os
import sys
import socketio
import cv2
import warnings

warnings.filterwarnings('ignore', category=FutureWarning)
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
from keras.models import load_model

CATEGORIES = ["forward", "right", "left", "backward", "stop", "still"]
MODEL_PATH = "workingDir + '/t11/McQueen_p3.model"
IMG_PATH = "workingDir + '/direction_api/directions/direction.jpg"
SOCKET_CHANNEL = "prediction"
SOCKET_SRV_URL = "http://localhost:3000"

sio = socketio.Client()
workingDir = os.path.dirname(os.path.realpath(sys.argv[0]))


def prep_img(file_path):
    IMG_SIZE = 100
    img_array = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    img = img_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    return img / 255


def predict(model_path, img):
    model = load_model(model_path)
    result = model.predict_classes(prep_img(img))
    return result[0]


@sio.event
def connect():
    # connect to running socket server
    sio.connect(SOCKET_SRV_URL)


@sio.on(SOCKET_CHANNEL)
def on_message(_):
    prediction = predict(MODEL_PATH, IMG_PATH)


connect()
