import os
import cv2
import matplotlib.pyplot as plt

os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"

from keras.models import load_model

CATEGORIES = ["forward", "right", "left", "backward", "stop", "still"]


def prep_img(filepath):
    IMG_SIZE = 100  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)  # read in the image, convert to grayscale
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize image to match model's expected sizing
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


def show_img(x):
    plt.imshow(x.reshape(100, 100), cmap='gray')
    plt.show()


def pred(model_path, img):
    model = load_model(model_path)
    predict = model.predict_classes(prep_img(img))
    print(CATEGORIES[predict[0]])


show_img(prep_img('imgs/cam1.jpg'))
pred('models/t9/McQueen_p3.model', 'imgs/cam1.jpg')
