#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# This is the python code for testing numpy.ndarray <--> mxnet.ndarray.NDArray transfer.
#
# Author: hudoudou love learning
# Time: 2018-03-30

import mxnet as mx
import numpy as np

# in python, Arrays should be constructed using array, zeros or empty,
# np.array is just a convenience function to create an ndarray, it is not a class itself.
# You can also create an array using np.ndarray, but it is not the recommended way.

# list -> mxnet.ndarray.NDArray
list_x = [[1, 2, 3], [4, 5, 6]]   # list
print "type(list_x): ", type(list_x)

MXNDArray_from_list = mx.nd.array(list_x)
print "type(MXNDArray_from_list): ", type(MXNDArray_from_list)

# np.ndarray(numpy.ndarray) -> mxnet.ndarray.NDArray
ndarray_x = np.array([[1, 2, 3], [4, 5, 6]])  # np.ndarray
print "type(ndarray_x): ", type(ndarray_x)

MXNDArray_from_nparray = mx.nd.array(ndarray_x)
print "type(MXNDArray_from_nparray): ", type(MXNDArray_from_nparray)

# mxnet.ndarray.NDArray -> numpy.ndarray
MXNDArray_x = mx.nd.array([[1, 2, 3], [4, 5, 6]])
print "type(MXNDArray_x): ", type(MXNDArray_x)
print "MXNDArray_x.shape: ", MXNDArray_x.shape

MXNDArray_y = MXNDArray_x + mx.nd.ones(MXNDArray_x.shape) * 3
nparray_z = MXNDArray_y.asnumpy() 
print "type(MXNDArray_y): ", type(MXNDArray_y)
print "type(nparray_z): ", type(nparray_z)

# other test
MXNDArray_A = mx.nd.ones((2, 3))
nparray_B = MXNDArray_A.asnumpy()
print "type(MXNDArray_A): ", type(MXNDArray_A)
print "type(nparray_B): ", type(nparray_B)

MXNDArray_C = mx.nd.ones((2, 3), dtype='int32')
MXNDArray_C.asnumpy()
print "type(NDArray_C): ", type(MXNDArray_C)
