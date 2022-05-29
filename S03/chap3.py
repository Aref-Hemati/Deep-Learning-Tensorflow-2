import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

x = np.linspace(0,4,120)
y = 2*x + 0.9 + np.random.randn(x.shape[0]) * 0.3
plt.scatter(x,y,label="input data set")
plt.show()

class Linearregmodel:
    def __init__(self):
        self.Weight = tf.Variable(5.0)
        self.Bias = tf.Variable(6.0)
    def __call__(self,x):
        return self.Weight*x + self.Bias

def loss(y,pred):
    return   tf.reduce_mean(tf.square(y-pred))

def train(linear_model,x,y,eta=0.12):
    with tf.GradientTape() as t:
        current_loss = loss(y,linear_model(x))

    lr_weight,lr_bias = t.gradient(current_loss,[linear_model.Weight,linear_model.Bias])
    linear_model.Weight.assign_sub(eta*lr_weight)
    linear_model.Bias.assign_sub(eta * lr_bias)

linear_model = Linearregmodel()
epochs = 100
for epoch_count in range(epochs):
    real_loss = loss(y,linear_model(x))
    train(linear_model,x,y,eta=0.12)
    print(f"Epoch count {epoch_count} : Loss value : {real_loss.numpy()}")




