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
import code_model
import code_train
import code_input_data


#数据集一     (图片的像素是展平的)
VALIDATION_IMAGES = code_train.VALIDATION_IMAGES
VALIDATION_LABELS = code_train.VALIDATION_LABELS
TEST_IMAGES = code_train.TEST_IMAGES
TEST_LABELS = code_train.TEST_LABELS

#数据集二   （图片的像素是三维的）
VALIDATION_IMAGES_3D = code_train.VALIDATION_IMAGES_3D
TEST_IMAGES_3D = code_train.TEST_IMAGES_3D

#读取持久化模型的间隔时间
INTERVAL_SEC = 5


def evaluate():
    with tf.Graph().as_default():
        x = tf.placeholder(tf.float32, [None, code_model.IMAGE_SIZE, code_model.IMAGE_SIZE, code_model.CHANNEL_NUM], "x_input")
        y = tf.placeholder(tf.float32, [None, code_model.OUTPUT_NUM], "y_input")

        pred_y = code_model.inference(x, None)

        correct_prediction = tf.equal(tf.argmax(pred_y, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        # 搞不懂下面这三行代码在干嘛。。。。
        variable_averages = tf.train.ExponentialMovingAverage(code_train.MOVING_AVERAGE_DECAY)
        variables_to_restore = variable_averages.variables_to_restore()
        saver = tf.train.Saver(variables_to_restore)

        while True:
            print("*"*80)
            with tf.Session() as sess:
                ckpt = tf.train.get_checkpoint_state(code_train.MODEL_PATH)
                if ckpt and ckpt.model_checkpoint_path:
                    saver.restore(sess, ckpt.model_checkpoint_path)
                    global_step = ckpt.model_checkpoint_path.split("/")[-1].split("-")[-1]
                    accuracy_score = sess.run(accuracy, feed_dict={x:VALIDATION_IMAGES_3D, y:VALIDATION_LABELS})

                    print("After %s training steps, accuracy score on test data is %s" % (global_step, accuracy_score))
                else:
                    print("No checkpoint file found")
                    return
            time.sleep(INTERVAL_SEC)


def main(argv=None):
    evaluate()

if __name__ == "__main__":
    tf.app.run()
