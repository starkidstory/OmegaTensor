import tensorflow as tf
import pathlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#print(np.version.version)
#np.set_printoptions(precision=4)

dataset=tf.data.Dataset.from_tensor_slices([8,3,0,8,2,1])
num=np.arange(5)
numT=tf.convert_to_tensor(num)
numF=tf.cast(numT,dtype=tf.float32)
print(numT)
print(numF)
print(dataset)
mat=tf.convert_to_tensor(np.zeros([3,3]))
print(mat)
small_list=tf.convert_to_tensor([1,2,3],dtype=tf.float64)
print(small_list)

print(np.random.randint(0,5))