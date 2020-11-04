'''
입력크기에 맞는 이미지로 바꾸고 랜덤하게 이미지 순서를 섞는 코드
'''
import numpy as np
import cv2, os, random
from PIL import Image

original_path = './datasets/tmp_images/hair1/'
new_path = './images/'

img_list = os.listdir(original_path)
n = len(img_list)
random.shuffle(img_list)
print(n)
num = int(0.7*n)

# train - hair
index = 1
train_hair_path = new_path+"train/hair/"
print(train_hair_path)
for name in img_list[:num] :
    img = Image.open('%s%s'%(original_path, name))
    img_array = np.array(img)
    img_size = img.size
    if img_size[0]*img_size[1] > 150*150:
        img_resize = cv2.resize(img_array, (150,150), interpolation = cv2.INTER_CUBIC)
    else:
        img_resize = cv2.resize(img_array, (150,150), interpolation = cv2.INTER_AREA)
    img = Image.fromarray(img_resize)
    try:
        img.save('%s%s'%(train_hair_path,name))
    except:
        img = img.convert("RGB")
        img.save('%s%s'%(train_hair_path,name))
        # print(img_size[0]*img_size[1],'은 error')
    # print(name + '   ' + str(index) + '/')
    # index +=1

# test - hair
test_hair_path = new_path+"test/hair/"
print(test_hair_path)
for name in img_list[num:] :
    img = Image.open('%s%s'%(original_path, name))
    img_array = np.array(img)
    img_size = img.size
    if img_size[0]*img_size[1] > 150*150:
        img_resize = cv2.resize(img_array, (150,150), interpolation = cv2.INTER_CUBIC)
    else:
        img_resize = cv2.resize(img_array, (150,150), interpolation = cv2.INTER_AREA)
    img = Image.fromarray(img_resize)
    try:
        img.save('%s%s'%(test_hair_path,name))
    except:
        img = img.convert("RGB")
        img.save('%s%s'%(test_hair_path,name))


# train - hair_loss 분류
original_path = './datasets/tmp_images/hair_loss1/'
new_path = './images/'

img_list = os.listdir(original_path)
n = len(img_list)
random.shuffle(img_list)
num = int(0.7*n)

# train - hair_loss 분류
train_hair_path = new_path+"train/hair_loss/"
for name in img_list[:num] :
    img = Image.open('%s%s'%(original_path, name))
    img_array = np.array(img)
    img_size = img.size
    if img_size[0]*img_size[1] > 150*150:
        img_resize = cv2.resize(img_array, (150,150), interpolation = cv2.INTER_CUBIC)
    else:
        img_resize = cv2.resize(img_array, (150,150), interpolation = cv2.INTER_AREA)
    img = Image.fromarray(img_resize)
    try:
        img.save('%s%s'%(train_hair_path,name))
    except:
        img = img.convert("RGB")
        img.save('%s%s'%(train_hair_path,name))

# test - hair_loss 분류
index = 1
test_hair_path = new_path+"test/hair_loss/"
# print(train_hair_path)
for name in img_list[num:] :
    img = Image.open('%s%s'%(original_path, name))
    img_array = np.array(img)
    img_size = img.size
    if img_size[0]*img_size[1] > 150*150:
        img_resize = cv2.resize(img_array, (150,150), interpolation = cv2.INTER_CUBIC)
    else:
        img_resize = cv2.resize(img_array, (150,150), interpolation = cv2.INTER_AREA)
    img = Image.fromarray(img_resize)
    try:
        img.save('%s%s'%(test_hair_path,name))
    except:
        img = img.convert("RGB")
        img.save('%s%s'%(test_hair_path,name))