#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/13 11:52
# @Author  : yuxin.wang
# @File    : demo_cnn.py
# @Project : m_weibo

from scipy.misc import imread
import numpy as np
import os
import keras

TRAIN_PATH = './train'

def load_train_data():
    img_list = [os.path.join(TRAIN_PATH, i) for i in os.listdir(TRAIN_PATH)]
    train_data_x = np.concatenate([np.expand_dims(imread(i), axis=0) for i in img_list], axis=0) / 255
    train_data_y = np.expand_dims(np.array([int(i[0]) - 1 for i in os.listdir(TRAIN_PATH)]), axis=-1)
    return train_data_x, train_data_y

def create_model():
    model = keras.models.Sequential()
    model.add(keras.layers.Conv2D(16, 3, padding='same', data_format='channels_last'))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.MaxPooling2D(3))
    model.add(keras.layers.Conv2D(32, 3, padding='same', data_format='channels_last', activation='relu'))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.MaxPooling2D(3))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(16, activation='relu'))
    model.add(keras.layers.Dense(4, activation='softmax'))
    model.compile('adam', loss=keras.losses.sparse_categorical_crossentropy, metrics=['accuracy'])
    return model

if __name__ == '__main__':
    _x, _y = load_train_data()
    print(_x.shape, _y.shape)
    model = create_model()
    model.fit(_x, _y, batch_size=4, epochs=200)