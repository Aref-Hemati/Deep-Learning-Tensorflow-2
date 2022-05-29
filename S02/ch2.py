import tensorflow as tf

c1 = tf.constant(5,tf.int16)
c2 = tf.constant([5,3,6],tf.int16)
c3 = tf.constant([[5,3,6],[4,8,9]],tf.int16)

print(c1)
print(c2)
print(c3)

v1 = tf.Variable(4,tf.int16)
v1.assign(5)

print(v1)

tfs = tf.sparse.SparseTensor([[0,0],[2,3]],[5,10],[3,4])

print(tfs)