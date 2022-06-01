import tensorflow as tf
from tensorflow import keras as ks
import numpy as np
import datetime

(train_data,train_labels),(test_data,test_labels) =ks.datasets.fashion_mnist.load_data()

train_data = train_data / 255.0
test_data = test_data / 255.0

input_data_shape = (28,28)
nn_model = ks.models.Sequential()

nn_model.add(ks.layers.Flatten(input_shape=input_data_shape))
nn_model.add(ks.layers.Dense(32,activation='relu'))
nn_model.add(ks.layers.Dense(10,activation='softmax'))

nn_model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir,histogram_freq=1)

nn_model.fit(train_data,train_labels,epochs=10,callbacks=[tensorboard_callback])
nn_model.fit(train_data,train_labels,epochs=10)

testdata_loss,testdata_accuracy=nn_model.evaluate(test_data,test_labels)
print('Test Data Accuracy {}'.format(round(float(testdata_accuracy),2)))



nn_model.save(f"./nnmodel/{1}",save_format='tf')