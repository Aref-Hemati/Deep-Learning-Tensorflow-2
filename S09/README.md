**cha9:**  Using Tensorboard (in example of Nural network definition in TensorFlow on fashion mnist dataset)

(Tensorboard is a tool for providing the measurements and visualizations needed during the machine learning workflow. It enables tracking experiment metrics like loss and accuracy, visualizing the model graph, projecting embeddings to a lower dimensional space, and much more)

- Define a dataset from Keras
- Data normalization 
- Define a sequential model with 3 layer
- Define an input layer
- Define middle layer as a dense layer by 'relu' activation function
- Define the output layer as a dense layer by 'softmax' activation function
- Define compile with 'adm' optimizer and 'sparse_categorical_crossentropy' as a loss  and 'accuracy' metrics
- Define path to log data (use time in the log)
- call tensorboard with defined path and plot histogram per execution
- Define a train function for data, set epochs, and set defined tensorboard callback
- Define an evaluation function for data
- Save model
- show tensorboard results:
```python
> Tensorbarod --logdir log-path
```
