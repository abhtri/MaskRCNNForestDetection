
'''import tensorflow'''

import flask
from flask import request, render_template,send_file
import base64
import cv2
import maskservice as ms
#import numpy as np
#import pandas as pd
'''from copy import deepcopy'''
#from werkzeug import secure_filename
app = flask.Flask(__name__)

@app.route("/")
def viz_page():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':  
        f = request.files['image']
        print('saving the uploaded image ')
        f.save('var/' + '1.jpg')
        img = ms.serviceImage1()
        cv2.imwrite('var/messigray.jpg',img)
        img1 = cv2.imread('var/messigray.jpg')
        print('image 1 read ')
        _, img_encoded = cv2.imencode('.jpg', img1)
        print('sending data back')
        return base64.b64encode(img_encoded)

@app.route('/hello', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['image']
        f.save('var/' + '1.jpg')
        #img = cv2.imread(os.path.join(folder,filename))
        img = cv2.imread('var/1.jpg')
        _, img_encoded = cv2.imencode('.jpg', img)
        return base64.b64encode(img_encoded)

if __name__ == '__main__':
    app.run(port=5000,debug=False, threaded=False)
''' app.run(port=5000, debug=True)''' 