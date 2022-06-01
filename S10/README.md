**Tensorflow Serving**

**cha9**
- use the model created in "S09/Cha9"
- Save model (set file path) with 'tf' file format

**Create a TensorFlow docker image from model**
``` 
> docker pull tensorflow/serving

> docker run -p 8501:8501 --mount type=bind,source= 'path of target folder', target='target file path' -e MODEL_NAME='Model Name' -t tensorflow/serving
```

**Create a TensorFlow docker image from model**

- load test data
- Data normalization
- create JSON request  data and use test data as an instance 
- create post request on localhost with defined port, model name, target function (predict), and defined JSON request  data
- load response and print it