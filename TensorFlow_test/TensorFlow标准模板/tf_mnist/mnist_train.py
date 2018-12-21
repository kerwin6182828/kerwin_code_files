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
#自己写的模块
import mnist_model
#导入数据集（免去了清洗的步骤）
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data", one_hot=True)


# 三种优化方法：(按出场顺序排列)
#1.惩罚率
REGULARA_RATE = 0.01
#2.学习率、学习率指数衰减率
LEARNING_RATE_BASE = 0.1
LEARNING_DECAY_STEP = 100
LEARNING_RATE_DECAY = 0.99
#3.指数平滑衰减率
MOVING_AVERAGE_DECAY = 0.9999

#训练指标
TRAINING_STEP = 600
BATCH_SIZE = 100

#数据集一     (图片的像素是展平的)
TRAIN_IMAGES = mnist.train.images
TRAIN_LABELS = mnist.train.labels
VALIDATION_IMAGES = mnist.validation.images
VALIDATION_LABELS = mnist.validation.labels
TEST_IMAGES = mnist.test.images
TEST_LABELS = mnist.test.labels

#数据集二   （图片的像素是三维的）
TRAIN_IMAGES_3D = TRAIN_IMAGES.reshape((-1, mnist_model.IMAGE_SIZE, mnist_model.IMAGE_SIZE, mnist_model.CHANNEL_NUM))
VALIDATION_IMAGES_3D = VALIDATION_IMAGES.reshape((-1, mnist_model.IMAGE_SIZE, mnist_model.IMAGE_SIZE, mnist_model.CHANNEL_NUM))
TEST_IMAGES_3D = TEST_IMAGES.reshape((-1, mnist_model.IMAGE_SIZE, mnist_model.IMAGE_SIZE, mnist_model.CHANNEL_NUM))


#模型的保存路径、文件名
MODEL_PATH = "./path/"
MODEL_NAME = "model.ckpt"

def train():
    with tf.Graph().as_default():
        global_step = tf.Variable(0, trainable=False)

        # 输入、输出占位符
        x = tf.placeholder(tf.float32, [None, mnist_model.IMAGE_SIZE, mnist_model.IMAGE_SIZE, mnist_model.CHANNEL_NUM], "x_input")
        y = tf.placeholder(tf.float32, [None, mnist_model.OUTPUT_NUM], "y_input")

        # 模型最终输出层（包含了优化1：惩罚项）
        logits = mnist_model.inference(x, REGULARA_RATE)

        # 优化2：学习率指数衰减
        learning_rate = tf.train.exponential_decay(LEARNING_RATE_BASE, global_step, LEARNING_DECAY_STEP, LEARNING_RATE_DECAY, staircase=True)
        tf.summary.scalar("learning_rate", learning_rate)

        # 优化3：指数平滑衰减（针对所有trainable的变量）
        variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
        variable_averages_op = variable_averages.apply(tf.trainable_variables())

        # 计算最终损失值
        cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.argmax(y, 1), name="cross_entropy_whole_example")
        cross_entropy_mean = tf.reduce_mean(cross_entropy, name="cross_entropy_mean")

        tf.add_to_collection('losses', cross_entropy_mean)
        loss = tf.add_n(tf.get_collection('losses'), name='total_loss')
        # loss = cross_entropy_mean + tf.add_n(tf.get_collection("losses"), name="final_loss")
        # loss = cross_entropy_mean

        # 算法：梯度下降（训练的op）
        optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)
        with tf.control_dependencies([optimizer, variable_averages_op]):
            train_op = tf.no_op(name="train") # 具体机制不清楚，但是可以知道它把“梯度下降”和”指数平滑” 捆绑在一起了。（这两个操作同步进行）


        saver = tf.train.Saver()
        with tf.Session() as sess:
            tf.global_variables_initializer().run()

            for i in range(TRAINING_STEP):
                start = (i * BATCH_SIZE) % TRAIN_IMAGES.shape[0]
                end = min(start + BATCH_SIZE, TRAIN_IMAGES.shape[0])
                xs, ys = TRAIN_IMAGES_3D[start:end], TRAIN_LABELS[start:end]
                _, l, step = sess.run([train_op, loss, global_step], feed_dict={x:xs, y:ys}) #写变量名的时候一定要注意不要重复！！！（md，被这“loss”坑惨了。。。）

                print(i)
                if i % 5 == 0:
                    print("After %d training steps, loss on training batch is %s" % (step, l))
                    saver.save(sess, os.path.join(MODEL_PATH, MODEL_NAME), global_step=global_step)


def main(argv=None):
    train()

if __name__ == "__main__":
    tf.app.run()
