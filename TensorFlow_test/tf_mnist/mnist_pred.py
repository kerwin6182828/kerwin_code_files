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
#自己写的模块
import mnist_model
import mnist_train


#输入待预测图像数据
INPUT_IMAGE = TEST_IMAGES_3D[:10]

def evaluate(input_image):
    with tf.Graph().as_default():
        x = tf.placeholder(tf.float32, [None, mnist_model.IMAGE_SIZE, mnist_model.IMAGE_SIZE, mnist_model.CHANNEL_NUM], "x_input")

        pred_y = mnist_model.inference(x, None)

        prediction = tf.argmax(pred_y, 1)

        # 搞不懂下面这三行代码在干嘛。。。。
        variable_averages = tf.train.ExponentialMovingAverage(mnist_train.MOVING_AVERAGE_DECAY)
        variables_to_restore = variable_averages.variables_to_restore()
        saver = tf.train.Saver(variables_to_restore)


        print("*"*80)
        with tf.Session() as sess:
            ckpt = tf.train.get_checkpoint_state(mnist_train.MODEL_PATH)
            if ckpt and ckpt.model_checkpoint_path:
                saver.restore(sess, ckpt.model_checkpoint_path)
                global_step = ckpt.model_checkpoint_path.split("/")[-1].split("-")[-1]
                predict_value = sess.run(prediction, feed_dict={x:input_image})

                print("After %s training steps, the FINAL PREDICTION of your input image is %s" % (global_step, predict_value))
                return predict_value
            else:
                print("No checkpoint file found")
                return



def main(argv=None):
    pred_value = evaluate(INPUT_IMAGE)

if __name__ == "__main__":
    tf.app.run()
