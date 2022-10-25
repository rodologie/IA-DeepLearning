# Practical Work 1 

**Academic year: 2022-2023**

## Goals
1.  Recalls on numpy, scikit-learn etc.
2.  Implementation of perceptron in Python
3.  Introduction to Tensorflow 2.0+.

## Exercise 1.1 [★]
Your first exercise consists of downloading the [Python Jupyter notebook](./practical1.ipynb) and familiarizing yourself with the different methods of the libraries: numpy, scikit-learn etc.

## Exercise 1.2 [★★]
Implement perceptron in Python with the following features
1. Configurable activation function
2. Configurable number of inputs 
3. Configurable number of epochs and training rates
4. Make predictions

Test your model with simple functions.


## Exercise 1.3 [★★★]
Upgrade tensorflow to the latest version.

```
              !pip install tensorflow --upgrade              
```

See the version installed on your machine

```
              import tensorflow as tf
              print(tf.__version__)              
```

For example, you may get the following value

```
              2.3.1             
```

![Artificial neural networks](Colored_neural_network.svg)

In order to create the above neural network model, you can test the
following code.

```
 from tensorflow.keras.models import Sequential
 from tensorflow.keras.layers import Conv2D
 from tensorflow.keras.layers import MaxPool2D
 from tensorflow.keras.layers import Flatten
 from tensorflow.keras.layers import Dense
 
 # Creating a sequential model
 model = Sequential()
 model.add(Dense(4, activation='relu', input_shape=(3,)))
 model.add(Dense(units=2, activation='softmax'))

 # compiling the model
 model.compile(loss='mse', optimizer='sgd', metrics=['accuracy'])
```

In the above model, we use Stochastic gradient descent optimizer and
mean square error as the loss calculator.

In the code below, we use a SGD optimizer using a learning rate of 0.01.

```
 from tensorflow.keras.models import Sequential
 from tensorflow.keras.layers import Conv2D
 from tensorflow.keras.layers import MaxPool2D
 from tensorflow.keras.layers import Flatten
 from tensorflow.keras.layers import Dense
 from tensorflow.keras.optimizers import SGD

 # Creating a sequential model
 model = Sequential() 
 model.add(Dense(4, activation='relu', input_shape=(3,)))
 model.add(Dense(units=2, activation='softmax'))

 # compiling the model
 sgd = SGD(lr=0.01)
 model.compile(loss='mean_squared_error', optimizer=sgd,metrics=['accuracy'])
```

Observe the different layers. Choose a dataset from Tensorflow:
<https://www.tensorflow.org/datasets/catalog/overview> and build a model
for your hypothesis. You can also make use of the existing models.


## Exercise 1.4 [★★★]
Create a neural network model using Tensorflow. Your goal is to configure the different parameters of your model and test it with the MNIST handwriting data set.
1. The number of hidden layers
2. The configuration of hidden layers such as the activation function
3. The dropout rate of your model
4. Optimization algorithms
5. Loss functions

Evaluate your model using the different indicators available (accuracy etc.).

