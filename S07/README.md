**chap7:** DCGAN in Tensorflow 2 on fashion MNist Dataset

- Define sie of the noise vector
- Load fashion MNist dataset
- Data normalization
- Use tf. data API enables you to build complex input pipelines from simple, reusable pieces
- The method shuffles the samples in the dataset. The buffer_size is the number of samples that are randomized and returned as tf


**Define Discriminator Network**
- Add four 2d convolution layers including Conv2D, BatchNormalization, LeakyReLU, and BatchNormalization
- Define the LeakReLU layer as a threshold : (Leaky Rectified Linear Unit, or Leaky ReLU, is a type of activation function based on a ReLU, but it has a small slope for negative values instead of a flat slope. The slope coefficient is determined before training, i.e. it is not learned during training)
- Define the dropout layer to avoid overfitting
- Define the BatchNormalization layer to normalize on data
- Define Globalmaxpooling
- Define output dense layer with 'sigmoid' activation



**Define Generator Network**
- Define a dense layer for noise
- Define the LeakyReLU layer to improve data
- Define reshape layer to convert to image format (3d)
- Define two Conv2DTranspose layers along with its LeakyRelu and BatchNormalization layers
- Define the convolution layer for the output layer

**Define DCGAN Network**
- Define DCGAN class that inherited from Keras.model with discriminator and generator functions input
-Define a compile function that inherited from compile method in the base class) to set optimizer both discriminator and generator 

- Define train function with  real images as input
- Make a random noise vector
- Call generator to generate fake images
- combine images of real and fake
- Set labels for real and fake images
- Add noise to labels to improvement
- Define train discriminator with combined images as input, find loss and calculate gradient base on it and discriminator wights 
- update optimizer discriminator wights

- Define train generator
- Make a random noise vector and 
- Set labels for fake images
- Define  train generator with combined noise vector as input, find loss and calculate gradient base on it and generator wights 


**Define Monitor Process And Show In Output**

- Define a class inherited Keras.callbacks.callback to show data after each epochs (on_epoch_vects)
- Generate fake images with a defined generator
- plot data generated fake images



**Define General**

- Define epochs
- Define dcgan from the defined function
- call compile of defined dcgan
- Call fit (inherited from the base class)