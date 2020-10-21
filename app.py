# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 09:37:10 2020

@author: ecemn
"""

from flask import Flask, render_template, request
#from keras.models import load_model
import tensorflow as tf
import numpy as np
import re
from keras.preprocessing import image
from skimage import transform
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import cv2 
from tensorflow.keras.models import Sequential 
from tensorflow.keras.layers import Dense


graph = tf.compat.v1.get_default_graph()

app = Flask(__name__)
loaded_model = load_model("models/binary_100epoch_saved.h5") 
loaded_model.run_eagerly = True
loaded_model.make_predict_function()

def image_preprocess(img):
  new_shape = (256, 256, 3)
  npimg = np.fromfile(img, np.uint8)
  img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
  image_array = image.img_to_array(img)
  image_array = transform.resize(image_array, new_shape, anti_aliasing = True)
  image_array /= 255
  image_array = np.expand_dims(image_array, axis = 0)
  return image_array

@app.route('/')
def home():
  return render_template("index.html")
@app.route('/result', methods=['POST','GET'])
def result():
    prediction=''

    if request.method == 'GET' or request.method == 'POST':
        img = request.files['pic']
        print(type(img))
        print(img)
        img_arr = image_preprocess(img)
        with graph.as_default():
           result = loaded_model.predict(img_arr)[0]

        print("result from model", result) 
        if result==0:
            prediction='boş'
        else:
            prediction='dolu'
        print(prediction)
        return render_template("result.html", prediction=prediction)

if __name__ == "__main__":
  app.run(debug=True)
