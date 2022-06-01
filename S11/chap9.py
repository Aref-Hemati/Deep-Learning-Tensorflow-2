import tensorflow as tf

converter = tf.lite.TFLiteConverter.from_saved_model('./nnmodelm/1')
tflite_model = converter.convert()
open("converted_modelch6.tflite","wb").write(tflite_model)
