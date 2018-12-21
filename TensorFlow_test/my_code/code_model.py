#标准模块、第三方模块
# import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd
import tensorflow as tf
# import sklearn
# import cv2
# from PIL import Image
# import math
# import os
# import re


#输入的节点数量
INPUT_NUM = 40*40
# 第一层卷积：
KERNEL1_NUM = 32
KERNEL1_SIZE = 5
# 第二层卷积：
KERNEL2_NUM = 64
KERNEL2_SIZE = 5
# 全连层的神经元数量：
FC1_NUM = 512
FC2_NUM = 256
#输出的节点数量
OUTPUT_NUM = 32

#图片的大小
IMAGE_SIZE = 40
#图片通道数
CHANNEL_NUM = 1




#这里的input_data是前向传播时候的data。
#（可以是train_images， 也可以说是test_images）----训练和测试用的都是这个前向传播的接口
def inference(input_data, regular_rate, dropout=None):

    with tf.variable_scope("conv1"):
        kernel = _get_variable_with_decay("kernel", shape=[KERNEL1_SIZE, KERNEL1_SIZE, CHANNEL_NUM, KERNEL1_NUM], stddev=5e-2, regular_rate=0.0)
        conv1 = tf.nn.conv2d(input_data, kernel, [1, 1, 1, 1], padding="SAME")
        biases = tf.get_variable("bias", [KERNEL1_NUM], initializer=tf.constant_initializer(0.0))
        conv1 = tf.nn.bias_add(conv1, biases)
        conv1 = tf.nn.relu(conv1, name="conv1")
        # _summary(conv1)
    with tf.variable_scope("pool1"):
        pool1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME", name="pool1")

    with tf.variable_scope("conv2"):
        kernel = _get_variable_with_decay("kernel", shape=[KERNEL2_SIZE, KERNEL2_SIZE, pool1.get_shape()[3], KERNEL2_NUM], stddev=5e-2, regular_rate=0.0)
        conv2 = tf.nn.conv2d(pool1, kernel, [1, 1, 1, 1], padding="SAME")
        biases = tf.get_variable("bias", [KERNEL2_NUM], initializer=tf.constant_initializer(0.0))
        conv2 = tf.nn.bias_add(conv2, biases)
        conv2 = tf.nn.relu(conv2, name="conv2")
        # _summary(conv2)
    with tf.variable_scope("pool2"):
        pool2 = tf.nn.max_pool(conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME", name="pool2")

    shape = pool2.get_shape()
    fc = shape[1:4].num_elements() # 就是把后面3个维度相乘（展平）
    flat = tf.reshape(pool2, (-1, fc))

    with tf.variable_scope("fc1"):
        weights = _get_variable_with_decay("weights", shape=[flat.get_shape()[1], FC1_NUM], stddev=0.04, regular_rate=0.004)  #这里有惩罚系数了(惩罚项一般只用在全连层)
        biases = tf.get_variable("bias", [FC1_NUM], initializer=tf.constant_initializer(0.1))  #这里的初始值设为了0.1
        fc1 = tf.nn.relu(tf.matmul(flat, weights) + biases, name="fc1")
        if dropout:
            fc1 = tf.nn.dropout(fc1, dropout)
        # _summary(fc1)

    with tf.variable_scope("fc2"):
        weights = _get_variable_with_decay("weights", shape=[fc1.get_shape()[1], FC2_NUM], stddev=0.04, regular_rate=0.004)  #这里有惩罚系数了(惩罚项一般只用在全连层)
        biases = tf.get_variable("bias", [FC2_NUM], initializer=tf.constant_initializer(0.1))  #这里的初始值设为了0.1
        fc2 = tf.nn.relu(tf.matmul(fc1, weights) + biases, name="fc2")
        if dropout:
            fc1 = tf.nn.dropout(fc1, dropout)
        # _summary(fc2)

    with tf.variable_scope("output"):
        weights = _get_variable_with_decay("weights", shape=[fc2.get_shape()[1], OUTPUT_NUM], stddev=0.04, regular_rate=0.0)  #这里有惩罚系数了(惩罚项一般只用在全连层)
        biases = tf.get_variable("bias", [OUTPUT_NUM], initializer=tf.constant_initializer(0.0))  #这里的初始值设为了0
        output_layer = tf.add(tf.matmul(fc2, weights), biases, name="output")# 此处没有relu
        # _summary(output_layer)

    return output_layer






def _get_variable_with_decay(name, shape, stddev, regular_rate):
    var = tf.get_variable(name, shape=shape, initializer=tf.truncated_normal_initializer(stddev=stddev))
    if regular_rate:
        regularizer = tf.contrib.layers.l2_regularizer(regular_rate)
        tf.add_to_collection("losses", regularizer(var))  # 如果有惩罚率的话，就创建惩罚项，并上传到tf管辖的集合上。（最后算loss的时候，再一并拉下来求和）
    return var


def _summary(tensor):
    tensor_name = re.sub("%s_[0-9]*/"%"tower", "", tensor.op.name)  # 没看明白
    tf.summary.scalar(tensor_name + "/sparsity", tf.nn.zero_fraction(tensor))
    tf.summary.histogram(tensor_name + "/activations", tensor)
