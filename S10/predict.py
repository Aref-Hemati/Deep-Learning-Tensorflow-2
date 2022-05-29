import json
import requests
import tensorflow as tf

(_,_),(test_data,test_labels) =tf.keras.datasets.fashion_mnist.load_data()
test_data = test_data / 255.0

data = json.dumps({"signature_name":"serving_default","instances":
                test_data[0].tolist()})
response = requests.request("POST","http://localhost:8501/v1/models/1:predict",data=data)
result = json.loads(response.text)
print(result)

