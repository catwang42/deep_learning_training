import numpy as np
import tensorflow as tf


a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a, b)
y = tf.multiply(a,b)
z = tf.pow(x,y)

with tf.Session() as sess:
	writer = tf.summary.FileWriter('./my_graphs', sess.graph) 
	print(sess.run(z))
writer.close() # close the writer when you’re done using it

