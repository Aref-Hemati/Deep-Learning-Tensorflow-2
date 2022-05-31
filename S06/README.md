**chap6:** Convolutional neural network in TensorFlow

- load CIFAR10 datasets from Keras
- Data Normalization of dataset images
- Define sequential model (VGG Neural Network) for future extraction
- Define the first Layer with 'relu' activation function, he_uniform  as a kernel initializer, and define input shap 
- Define the second layer as the same as the first layer (without input shape)
- define the max pooling layer to create a downsampled (pooled) feature map
- Define these layers two times more (based on VGG NN), with increased kernel numbers 
- Convert matrix data to vector data by flatten
- Define a sequential model  for future training
- Define a dense layer with 'relu' activation function and he_uniform  as a kernel initializer 
- Define an output dense layer with a softmax activation function
- Define stochastic gradient descent (SGD )optimizer 
- Model compile with the defined optimizer, loss function, and metrics (A metric is a function that is used to judge the performance of your model. Metric functions are similar to loss functions, except that the results from evaluating a metric are not used when training the model. Note that you may use any loss function as a metric.)
- train model with train data and set epochs for repeat count and batch size (to define the count of input images), Moreover Define validation data 
- evaluate model by test data
