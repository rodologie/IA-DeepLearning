Année: 2020-2021
----------------

# Travaux pratiques 2

## Objectifs
* Tensorflow
* Analyses de textes
* Modèles LSTM

## Exercice 2.1


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


## Exercice 2.2

Téléchargez une page HTML sur Internet (par ex, <https://en.wikipedia.org/wiki/Paris>).
Choisissez un long paragraphe de la page et effectuer les opérations suivantes

1.  Racinisation
2.  Étiquetage en parties du discours (PoS)
3.  Lemmatisation
4.  Analyse morphologique
5.  Reconnaissance d'entités nommées
6.  Word embeddings à l'aide de modèles Word2Vec (CPOW et Skip-gram)

Vous pouvez utiliser un ou plusieurs des packages suivants, dans la mesure du possible. Si
vous utilisez plus de deux packages, rédigez également un petit rapport sur la comparaison de vos résultats. 

1. nltk
2. spaCy
3. gensim
4. Tensorflow

## Exercice 2.3

### Modèles LSTM

**Prévision des séries temporelles avec les modèles LSTM** : Veuillez vérifier et lancer le code suivant
<https://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/>

Observez comment les séquences sont générées dans ces exemples.

