#标准模块、第三方模块
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import tensorflow as tf
# import sklearn
import cv2
# from PIL import Image
# import math
import os




def input_data_build():

    dir_lst = os.listdir(os.getcwd()+r"\train")
    dir_lst = [i for i in dir_lst if os.path.isdir(os.getcwd()+r"/train/"+ i)]
    print(dir_lst)

    train_images = []
    train_labels = []
    for dir in dir_lst:
        for img in os.listdir(os.getcwd()+r"/train/"+dir):
            print(img)
            im = cv2.imread("./train/%s/%s" % (dir, img), 0).reshape(-1)
            print(im)
            print("------")
            train_images.append(im)
            train_labels.append(dir)
    train_images = np.array(train_images)
    train_labels = np.array(train_labels)
    print(train_images.shape)
    print(train_labels.shape)
    train_labels_dummy = pd.get_dummies(train_labels)
    print(train_labels_dummy)
    print(train_labels_dummy.shape)
    labels_col = train_labels_dummy.columns
    print(labels_col)

    return(train_images, train_labels_dummy, labels_col) # （图像像素列表，DF对象， 所有标签名的lst）



def validation_data():
    dir_lst = os.listdir(os.getcwd()+r"\validation")
    dir_lst = [i for i in dir_lst if os.path.isdir(os.getcwd()+r"/validation/"+ i)]
    print(dir_lst)

    validation_images = []
    validation_labels = []
    for dir in dir_lst:
        for img in os.listdir(os.getcwd()+r"/validation/"+dir):
            print(img)
            im = cv2.imread("./validation/%s/%s" % (dir, img), 0).reshape(-1)
            print(im)
            print("------")
            validation_images.append(im)
            validation_labels.append(dir)
    validation_images = np.array(validation_images)
    validation_labels = np.array(validation_labels)
    print(validation_images.shape)
    print(validation_labels.shape)
    validation_labels_dummy = pd.get_dummies(validation_labels)
    print(validation_labels_dummy)
    print(validation_labels_dummy.shape)
    # labels_col = validation_labels_dummy.columns
    # print(labels_col)

    return(validation_images, validation_labels_dummy) # （图像像素列表，DF对象， 所有标签名的lst）



def test_data():
    test_images = []

    for img in os.listdir("test"):
        print(img)
        im = cv2.imread("./test/%s" % img, 0).reshape(-1)
        print(im)
        print("------")
        test_images.append(im)
    test_images = np.array(test_images)
    print(test_images.shape)
    print(test_images)

    return test_images





def main():
    input_data_build()
    # validation_data()
    # test_data()

if __name__ == "__main__":
    main()
