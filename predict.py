# '''
# 이미지 예측하는 코드
# '''
import os, re, glob
import cv2
import numpy as np
import shutil
from numpy import argmax
from keras.models import load_model
 
def Dataization(img_path):
    image_w = 150
    image_h = 150
    img = cv2.imread(img_path)
    img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0])
    return (img/255)
 
src = []
name = []
test = []
image_dir = "./images/real_test/"
for file in os.listdir(image_dir):
    # if (file.find('.png') is not -1):      
    src.append(image_dir + file)
    name.append(file)
    tmp = Dataization(image_dir + file)
    test.append(tmp)

test = np.array(test)
model = load_model('v6-2.h5')
predict = model.predict(test)
print(predict,name)
for i in range(len(test)):
    print(name[i],"님의 탈모 예측은",predict[i], " 입니다")