# Practical Work 1 

**Academic year: 2022-2023**

## Goals
1.  Recalls on numpy, scikit-learn etc.
2.  Implementation of perceptron in Python
3.  Introduction to Tensorflow 2.0+.

## Exercise 1.1 [★]
Your first exercise consists of downloading the [Python Jupyter notebook](./practical1.ipynb) and familiarizing yourself with the different methods of the libraries: numpy, scikit-learn etc. 

Download this webpage of Wikipedia: https://fr.wikipedia.org/wiki/Paris and save the file as an HTML. Analyze and identify all the possible tasks on this page. Write a program to implement these tasks. Possible tasks include the following:
- Extracting and analyzing words (occurrence count), links (anchor links, internal and external), and images (size)
- Extracting and identifying the numbers, dates, geographical coordinates, proper nouns (names of persons and places)
- Identifying and extracting the structured data including tables
- Differentiating the section and paragraphs

## Exercise 1.2 [★★]
Continuing with the downloaded Wikipedia page analyses, write a program to implement the following tasks.
-	Apply the stemmer algorithms PorterStemmer and SnowballStemmer on the text of the Wikipedia page. Recall that the Porter Stemming algorithm was created for the English language. Compare the outputs of both algorithms, especially the occurrence of the most common stems and the count of unique stems. 
-	Extract all the 1-gram (word), 2-grams (bi-gram), 3-grams, 4-grams, and 5-grams on the Wikipedia text and display the n most common occurrences of each. 
-  PoS Tagging
-  Lemmatization
-  Morphological analysis
-  Named Entity Recognition
-  Word embedding using Word2Vec models (CPOW and Skip-gram)

You can use one or more of the following packages, wherever possible. If
you are using more than two packages, also write a small comparative
report on your results.

1.  nltk
2.  spaCy
3.  gensim

## Exercise 1.3 [★★]
Implement perceptron in Python with the following features
1. Configurable activation function
2. Configurable number of inputs 
3. Configurable number of epochs and training rates
4. Make predictions

Test your model with simple functions.

## Exercise 1.4 [★★★]
Create a neural network model using Tensorflow. Your goal is to configure the different parameters of your model and test it with the MNIST handwriting data set.
1. The number of hidden layers
2. The configuration of hidden layers such as the activation function
3. The dropout rate of your model
4. Optimization algorithms
5. Loss functions

Evaluate your model using the different indicators available (accuracy etc.).

