import tensorflow as tf
import timeit

@tf.function
def function1(a,b):
    return a*b

def function2(a,b):
    return a*b

f2 = tf.function(function2)

a = tf.constant(2.0)
b = tf.constant(5.0)

print(function1(a,b))
print(f2(a,b))

class Sequentialmodel(tf.keras.Model):
    def __init__(self,**kwargs):
        super(Sequentialmodel,self).__init__(**kwargs)
        self.flatten = tf.keras.layers.Flatten(input_shape=(28,28))
        self.dense_1 = tf.keras.layers.Dense(128,activation='relu')
        self.dropout = tf.keras.layers.Dropout(0.2)
        self.dense_2 = tf.keras.layers.Dense(10)

    def call(self,x):
        x = self.flatten(x)
        x = self.dense_1(x)
        x = self.dropout(x)
        x = self.dense_2(x)
        return x

input_data = tf.random.uniform([60,28,28])

eager_model = Sequentialmodel()
graph_model = tf.function(eager_model)

print("Eager time:",timeit.timeit(lambda :eager_model(input_data),number=10000))
print("Graph time:",timeit.timeit(lambda :graph_model(input_data),number=10000))


