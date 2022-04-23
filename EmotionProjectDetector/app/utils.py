
from keras.models import load_model
from keras.models import Sequential
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os


haar = cv2.CascadeClassifier('/Users/maria/PycharmProjects/EmotionProjectDetector/model/haarcascade_frontalface_default.xml')

model = load_model('Users/maria/PycharmProjects/EmotionProjectDetector/model/CK+_model.h5')

print('Model loaded sucessfully')

prediction = ['angry','neutral','disgust','fear','happy','sad','surprise']
font = cv2.FONT_HERSHEY_SIMPLEX




def Predict_model(path, filename, color='bgr'):
    # step-1: read image in cv2
    img = cv2.imread(path)
    # step-2: convert into gray scale
    if color == 'bgr':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # step-3: crop the face (using haar cascase classifier)
    faces = haar.detectMultiScale(gray, 1.5, 3)
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)  # drawing rectangle
        roi = gray[y:y + h, x:x + w]  # crop image
        # step - 4: normalization (0-1)
        # roi = roi / 255.0
        # step-5: resize images (100,100)
        # if roi.shape[1] > 100:
            # roi_resize = cv2.resize(roi, (100, 100), cv2.INTER_AREA)
        # else:
            # roi_resize = cv2.resize(roi, (100, 100), cv2.INTER_CUBIC)
        # step-6: Flattening (1x10000)
        # roi_reshape = roi_resize.reshape(1, 10000)  # 1,-1
        # step -9: pass to ml model (svm)
        results = model.predict(roi)[0]
        # step -10:
        predict = results.argmax()  # 0 or 1
        # score = results[predict]
        # step -11:
        # text = "%s : %0.2f" % (prediction[predict], score)
        # cv2.putText(img, text, (x, y), font, 1, (255, 255, 0), 2)

    cv2.imwrite('/Users/maria/PycharmProjects/EmotionProjectDetector/static/predict/{}'.format(filename), img)


