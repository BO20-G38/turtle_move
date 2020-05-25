from keras.models import load_model
import os
import time
import sys
import subprocess as sp
import cv2
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"


CATEGORIES = ["forward", "right", "left", "backward", "stop", "still"]


def prep_img(filepath):
    IMG_SIZE = 100
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    img = img_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    return img / 255


def pred(model_path, img):
    model = load_model(model_path)
    predict = model.predict_classes(prep_img(img))
    return predict[0]


workingDir = os.path.dirname(os.path.realpath(sys.argv[0]))
prediction = pred(workingDir + '/t11/McQueen_p3.model',
                  workingDir + '/direction_api/directions/direction.jpg')

sys.stdout.write(str(prediction))
