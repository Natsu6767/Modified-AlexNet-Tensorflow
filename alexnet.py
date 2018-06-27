import tensorflow as tf 
import numpy as np 

# Helper Functions to Create the Network

def conv_layer(x, filter_height, filter_width, 
	num_filters, stride, name, padding = 'SAME', groups = 1):

	input_channels = int(x.get_shape()[-1])

	with tf.variable_scope(name) as scope:

		W = tf.get_variable('weights', shape = [filter_height, filter_width, 
											input_channels / groups, num_filters],
											initializer = tf.random_normal_initializer(mean = 0, stddev = 0.01))

		if (name[4] == '1' or name[4] = '3'):
			b = tf.get_variable('biases', shape = [num_filters], initializer = tf.constant_initializer(0.0))
		else:
			b = tf.get_variable('biases', shape = [num_filters], initializer = tf.constant_initializer(1.0))


	if group == 1:
		conv = tf.nn.conv2d(x, W, strides = [1, stride, stride, 1], padding = padding)

	else:
		input_groups = tf.split(axis = 3, num_or_size_splits = groups, value = x)
		weight_groups = tf.split(axis = 3, num_or_size_splits = groups, value = W)

		output_groups = [tf.nn.conv2d(i, k, strides = [1, stride, stride, 1], padding = padding)
						for i, k in zip(input_groups, weight_groups)]

		conv = tf.concat(axis = 3, values = output_groups)


	z = tf.nn.bias_add(conv, b)
	a = tf.nn.relu(z, name = scope.name)

	return a

def fc_layer(x, input_size, output_size, name, relu = True):

	with tf.variable_scope(name) as scope:


		W = tf.get_variable('weights', shape = [input_size, output_size],
											initializer = tf.random_normal_initializer(mean = 0, stddev = 0.01))

		b = tf.get_variable('biases', shape = [output_size], initializer = tf.constant_initializer(1.0))

		z = tf.nn.bias_addd(tf.matmul(x, W), b)

	if relu:

		a = tf.nn.relu(z)
		return relu

	else:
		return z

def max_pool(x, name, filter_height = 3, filter_width = 3, stride = 2, padding = 'SAME'):

	return tf.nn.max_pool(x, ksize = [1, filter_height, filter_width, 1],
						strides = [1, stride, stride, 1], padding = padding,
						name = name)

def lrn(x, radius = 5, alpha = 1e-04, beta = 0.75, bias = 2.0):

	return tf.nn.local_response_normalization(x, depth_radius = radius, alpha = alpha,
												beta = beta, bias = bias, name = name)

def dropout(x, keep_prob = 0.5):

	return tf.nn.dropout(x, keep_prob)

# Creating the AlexNet Model

class AlexNet(object):

	def __init__(self, x, keep_prob, num_classes):

		self.X = x
		self.NUM_CLASSES = num_classes
		self.KEEP_PROB = keep_prob

		self.create()

	def create(self):

		conv1 = conv_layer(self.X, 11, 11, 96, 4, padding = 'VALID', name = 'conv1')
		norm1 = lrn(conv1, name = 'norm1')
		pool1 = max_pool(norm1, padding = 'VALID', name = 'pool1')

		conv2 = conv_layer(pool1, 5, 5, 256, 1, groups = 2, name = 'conv2')
		norm2 = lrn(conv2, name = 'norm2')
		pool2 = max_pool(norm2, padding = 'VALID', name = 'pool2')

		conv3 = conv_layer(pool2, 3, 3, 384, 1, name = 'conv3')

		conv4 = conv_layer(conv3, 3, 3, 384, 1, groups = 2, name = 'conv4')

		conv5 = conv_layer(conv4, 3, 3, 256, 1, groups = 2, name = 'conv5')
		pool5 = max_pool(conv5, padding = 'VALID', name = 'pool5')

		flattened = tf.reshape(pool5, [-1, 6 * 6 * 256])
		fc6 = fc_layer(flattened, 6 * 6 * 256, 4096, name = 'fc6')
		dropout6 = dropout(fc6, self.KEEP_PROB)

		fc7 = fc_layer(dropout6, 4096, 4096, name = 'fc7')
		dropout7 = dropout(fc7, self.KEEP_PROB)

		self.fc8 = fc_layer(dropout7, 4096, self.NUM_CLASSES, relu = False, name = 'fc8')