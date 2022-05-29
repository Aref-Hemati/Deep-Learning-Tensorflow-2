import tensorflow as tf

@tf.function
def test(c1,c2):
    c3 = tf.multiply(c1,c2)
    return c3

c1 = tf.constant(5,tf.int16)
c2 = tf.constant(5,tf.int16)
c3 = test(c1,c2)
tf.print(c3)