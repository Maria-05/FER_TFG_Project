from flask import render_template, request
from flask import redirect, url_for
import os
from PIL import Image
from flask import render_template, request
from app.utils import Predict_model

UPLOAD_FLODER = '/Users/maria/PycharmProjects/EmotionProjectDetector/static/uploads'

def base():
    return render_template('base.html')

def index():
    return render_template('index.html')

def project():
    return render_template('project.html')

def pasos():
    return render_template('pasos.html')

def detector():
    return render_template('detector.html')

def getwidth(path):
    img = Image.open(path)
    size = img.size # width and height
    aspect = size[0]/size[1] # width / height
    w = 300 * aspect
    return int(w)

def emotion():

        if request.method == "POST":
            f = request.files['image']
            filename=  f.filename
            path = os.path.join(UPLOAD_FLODER,filename)
            f.save(path)
            w = getwidth(path)
            predict_model(path, filename, color='bgr')
            return render_template('emotion.html', fileupload=True, img_name=filename, w=w)

        return render_template('emotion.html', fileupload=False, img_name="emotion.png")
