Année: 2021-2022
----------------

# Travaux pratiques 1

## Objectifs

1.  Rappels sur numpy, pandas, scikit-learn etc.
2.	Implémentation de perceptron en Python
3.	Introduction à Tensorflow 2.0+

## Exercice 1.1 [★]
Votre premier exercice consiste à télécharger le [notebook Python Jupyter](TP1.ipynb) et à vous familiariser avec les différentes méthodes des bibliothèques: numpy, pandas, scikit-learn etc.

## Exercice 1.2 [★★]
Implémenter perceptron en Python avec les caractéristiques suivantes
1. Fonction d'activation configurable
2. Nombre d'entrées configurables 
3. Nombre d'époques et taux de formation configurables
4. Effectuer des prévisions

Tester votre modèle avec des fonctions simple.

## Exercice 1.3 [★★★]
Mettez à jour tensorflow avec la dernière version.
```
              !pip install tensorflow --upgrade              
```

Voir la version installée sur votre machine

```
              import tensorflow as tf
              print(tf.__version__)              
```

Par exemple, vous pouvez voir la valeur suivante (2.0+)

```
              2.3.1             
```

![Artificial neural networks](../../en/practical2/Colored_neural_network.svg)

Afin de créer le modèle de réseau neuronal ci-dessus, vous pouvez tester le
code suivant.

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

Dans le modèle ci-dessus, nous utilisons l'optimiseur de descente de gradient stochastique et
l'erreur quadratique moyenne comme calculateur de perte.

Dans le code ci-dessous, nous utilisons un optimiseur SGD utilisant un taux d'apprentissage de 0,01.

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

Observez les différentes couches. Choisissez un ensemble de données de Tensorflow :
<https://www.tensorflow.org/datasets/catalog/overview> et construisez un modèle
pour votre hypothèse. Vous pouvez également utiliser les modèles existants.

## Exercice 1.4 [★★★]
Créer un modèle de réseau de neurones en utilisant Tensorflow. Votre objectif est de configurer les différents paramètres de votre modèle et tester le modèle avec l'ensemble de données d'écriture manuscrite du MNIST.
1. Le nombre de couches cachées
2. La configuration des couches cachées comme la fonction d'activation
3. Le taux d'abandon de votre modèle
4. Algorithmes d'optimisation
5. Fonctions de perte

Évaluez votre modèle en utilisant les différents indicateurs disponibles (précision etc.)
