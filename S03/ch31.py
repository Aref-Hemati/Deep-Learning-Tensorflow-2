import tensorflow as tf

tf.compat.v1.disable_eager_execution()

c1 = tf.constant(5,tf.int16)
c2 = tf.constant(11,tf.int16)

c3 = tf.multiply(c1,c2)

sess = tf.compat.v1.Session()
result = sess.run(c3)

print(result)
