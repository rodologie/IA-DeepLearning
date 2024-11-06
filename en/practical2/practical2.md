# Practical Work 2

**Academic year: 2024-2025**


### Goals
1. **Knowledge Modeling and Data Querying**: Use a logical language to structure a knowledge base and create rules to extract specific information from the data.

2. **Text and Image Classification**: Design and train neural network models for text classification (exercise 2.2) and image classification (exercise 2.4), focusing on data preprocessing, hyperparameter optimization, and model performance evaluation.

3. **Sequence Prediction**: Develop a model for translation sequence prediction, applying sequential data preparation techniques and evaluating model performance on test data.

## Exercise 2.1
You need to model a knowledge base for a school using GNU Prolog. This base should contain the following information:
- Students and their personal information (name, surname, date of birth, etc.).
- The project groups to which students belong.
- Management of students' grades in different subjects.
- A list of subjects with their names and descriptions.

1. **Describe the facts and rules** needed to represent this information in your Prolog program.

2. **Write a program in Prolog** containing example data and rules. For example, you could include:
   - A rule to find all students in a specific project group.
   - A rule to calculate the average grades of a student in a subject.
   - A rule to list the subjects a student is enrolled in.

3. **Show examples of queries** to retrieve information from the knowledge base (for example, getting the list of students in a group or obtaining a student’s average grade). 

## Exercise 2.2
Check the following classification examples with deep neural networks using TensorFlow. 

- [Data Processing in TensorFlow](../Projet/Data.ipynb)
- [Handwritten Digit Recognition using the MNIST dataset](../Projet/Introduction.ipynb)
- [Text Classification using IMDB Reviews](../Projet/Textes.ipynb)

**Question:**
You will work on a text classification example using the **Reuters** dataset available in TensorFlow. This dataset contains news articles categorized into different topics, making it an excellent dataset for text classification.

Your task is to explore this dataset and develop a text classification model using deep neural networks in TensorFlow. You have the following objectives:

### Objectives:

1. **Loading and Preprocessing Data**:
   - Load the **Reuters** dataset using `tf.keras.datasets.reuters`.
   - Preprocess the data by converting the texts into sequences of numerical tokens compatible with the model. Use techniques like tokenization and padding to ensure uniform sequence lengths.
   - **Tips**: Use `Tokenizer` from `tf.keras.preprocessing.text` to transform texts into numerical sequences, and `pad_sequences` to standardize sequence lengths.

2. **Building a Neural Network Model**:
   - Create a deep neural network model for text classification. Experiment with different layer types to find an appropriate architecture (e.g., embedding layers for words, dense layers, or LSTM or GRU layers to capture sequence structures).
   - **Tips**: Start with a simple architecture (like a combination of Embedding and Dense layers), then explore adding recurrent layers for better word context understanding.

3. **Hyperparameter Optimization**:
   - Modify the model’s hyperparameters (e.g., number of neurons, number of layers, learning rate, number of epochs) and observe their impact on model performance.
   - **Tips**: Start with a basic learning rate (e.g., 0.001) and adjust based on convergence speed. Also experiment with different batch sizes and observe their effects.

4. **Model Training and Evaluation**:
   - Train your model using the Reuters data and evaluate its performance in terms of accuracy, recall, and F1 score.
   - **Tips**: Use `classification_report` from `sklearn.metrics` for a detailed classification report and Keras `history` to visualize accuracy and loss over training.

5. **Result Analysis and Visualization**:
   - Compare the performance of different configurations tested. Include graphs to show accuracy and loss over epochs for each configuration.
   - **Tips**: Use plots to represent training and validation accuracy over epochs and compare models to see how architecture and hyperparameter choices affect results.

6. **Document Observations and Conclusions**:
   - Document the configurations tested (layer types, hyperparameters, etc.), the results obtained, and observations on model performance based on adjustments made.

## Exercise 2.3
In this exercise, you will use the **CIFAR-10** dataset from TensorFlow to build and evaluate a convolutional neural network (CNN) model capable of classifying images into 10 categories (airplanes, cars, birds, cats, etc.).

### Objectives

1. **Loading and Preprocessing Data**:
   - Load the CIFAR-10 dataset from `tf.keras.datasets.cifar10`. This dataset contains 60,000 32x32 pixel images divided into 10 classes, with 50,000 images for training and 10,000 for testing.
   - Normalize the pixel values of the images between 0 and 1 to facilitate learning.
   - Apply data augmentation techniques to make the model more robust. Use transformations such as rotation, zoom, and horizontal flipping to increase the diversity of the training images.

2. **Creating a Convolutional Neural Network (CNN) Model**:
   - Design a CNN model using convolutional and pooling layers to extract important features from the images.
   - Suggested structure:
     - **Convolutional Layer**: Multiple filters (e.g., 32, 64, 128) with a small filter size (3x3), followed by ReLU activation.
     - **Pooling Layer**: Reduce the size of feature maps to decrease complexity (e.g., 2x2 max pooling).
     - **Dense Layers**: After the convolutional layers, flatten the feature maps and add one or more fully connected layers for classification.
     - **Regularization**: Integrate regularization techniques such as dropout or batch normalization to prevent overfitting.
   - Test different architectures by adding or removing layers to observe their impact on performance.

3. **Training and Optimizing the Model**:
   - Train the model using the `sparse_categorical_crossentropy` loss function, as this is a multiclass classification problem.
   - Use the Adam optimizer and experiment with different learning rates to see their effect on convergence (e.g., start with 0.001).
   - Adjust other hyperparameters like batch size and the number of epochs to find an optimal configuration that balances accuracy and computation time.

4. **Evaluating and Analyzing Performance**:
   - Evaluate the model on the test set and calculate overall accuracy as well as accuracy for each class.
   - Generate a classification report (e.g., with `classification_report` from `sklearn.metrics`) and a confusion matrix to identify classes where the model performs well and areas where improvements are possible.

5. **Documenting and Visualizing Results**:
   - Document the configurations tested (number of layers, hyperparameters, etc.) and the performance achieved.
   - Visualize training and validation accuracy and loss curves over epochs to analyze the model's learning behavior.
   - Display examples of correct and incorrect predictions to better understand the model's errors and identify ways to improve it.

## Exercise 2.4
[Mini Project - Understanding the Translation of Wikidata Properties](../Projet/miniprojet-notebook.ipynb)

For this mini-project, you will test deep learning models to predict possible translation sequences based on Wikidata properties.

#### Context

Consider the following sequence entered by the user:

```
['it', 'fi']
```

Your model should be able to predict the next language in the sequence, for example:

```
['fr']
```

### Task

Your goal is to train a neural network model capable of predicting the probable next translations for labels, descriptions, or aliases. To do this, follow the steps below:

1. **Data Preparation**:
   - Use the translation sequence of Wikidata properties as your dataset.
   - Split the sequences into training and test sets.

2. **Modeling**:
   - Implement a neural network model.

3. **Evaluation**:
   - After training the model, evaluate its performance on the test set.
   - Provide metrics such as accuracy and any other relevant measurements to assess the quality of the predicted translations.

### Guidelines

- Consider preprocessing your data, including cleaning entries and normalizing them.
- To improve your model’s performance, consider adjusting hyperparameters and testing different architectures.

## References
- [Multilayer Perceptron Explained with a Real-Life Example and Python Code: Sentiment Analysis](https://towardsdatascience.com/multilayer-perceptron-explained-with-a-real-life-example-and-python-code-sentiment-analysis-cb408ee93141)
- **Time Series Prediction with LSTM models**: [Time Series Prediction with LSTM Recurrent Neural Networks in Python with Keras](https://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/)
