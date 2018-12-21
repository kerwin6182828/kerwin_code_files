#标准模块、第三方模块
# import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
import tensorflow as tf
# import sklearn
# import cv2
# from PIL import Image
# import math
import os
import time

import code_input_data
import code_model
import code_train

# 这里的input_data 就是实战中，要我真正去预测的验证码的图片
input_data = code_train.TEST_IMAGES
labels_col = code_train.LABELS_COL

#数据集一     (图片的像素是展平的)
TRAIN_IMAGES = code_train.TEST_IMAGES   ## 这里的 TRAIN_IMAGES 就是实战中，要我真正去预测的验证码的图片
LABELS_COL = code_train.LABELS_COL


#数据集二   （图片的像素是三维的）
TRAIN_IMAGES_3D = TRAIN_IMAGES.reshape((-1, code_model.IMAGE_SIZE, code_model.IMAGE_SIZE, code_model.CHANNEL_NUM))

#输入待预测图像数据
def evaluate(input_image):
    with tf.Graph().as_default():
        x = tf.placeholder(tf.float32, [None, code_model.IMAGE_SIZE, code_model.IMAGE_SIZE, code_model.CHANNEL_NUM], "x_input")

        pred_y = code_model.inference(x, None)

        prediction = tf.argmax(pred_y, 1)

        # 搞不懂下面这三行代码在干嘛。。。。
        variable_averages = tf.train.ExponentialMovingAverage(code_train.MOVING_AVERAGE_DECAY)
        variables_to_restore = variable_averages.variables_to_restore()
        saver = tf.train.Saver(variables_to_restore)


        print("*"*80)
        with tf.Session() as sess:
            ckpt = tf.train.get_checkpoint_state(code_train.MODEL_PATH)
            if ckpt and ckpt.model_checkpoint_path:
                saver.restore(sess, ckpt.model_checkpoint_path)
                global_step = ckpt.model_checkpoint_path.split("/")[-1].split("-")[-1]
                predict_value = sess.run(prediction, feed_dict={x:input_image})

                print("After %s training steps, the FINAL PREDICTION of your input image is %s" % (global_step, LABELS_COL[predict_value]))
                return predict_value
            else:
                print("No checkpoint file found")
                return



def main(argv=None):
    #输入待预测图像数据
    pred_value = evaluate(TRAIN_IMAGES_3D)

if __name__ == "__main__":
    tf.app.run()
