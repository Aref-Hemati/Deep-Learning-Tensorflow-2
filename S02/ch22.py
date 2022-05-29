import tensorflow as tf

c1 = tf.constant(5,tf.int16)
c2 = tf.constant(5,tf.int16)

c3 = tf.multiply(c1,c2)

tf.print(c3)