# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:39:46 2020

@author: TY
"""


import tensorflow as tf

version = tf.__version__
gpu_ok = tf.test.is_gpu_available()

print("tf version:",version,"\nuse GPU",gpu_ok)