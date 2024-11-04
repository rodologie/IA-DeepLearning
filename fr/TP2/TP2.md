# Travaux pratiques 2

**Année: 2024-2025**

## Objectifs

1. **Modélisation de connaissances et interrogation de données** : Utiliser un langage logique pour structurer une base de connaissances et créer des règles permettant d’extraire des informations spécifiques à partir des données.

2. **Classification de textes et d'images** : Concevoir et entraîner des modèles de réseaux de neurones pour la classification de textes (exercice 2.2) et d'images (exercice 2.4), en maîtrisant le prétraitement des données, l'optimisation des hyperparamètres, et l'évaluation des performances des modèles.

3. **Prédiction de séquences** : Développer un modèle de prédiction pour des séquences de traductions, en appliquant des techniques de préparation de données séquentielles et en évaluant les performances du modèle sur des données de test.

## Exercice 2.1

Vous devez modéliser une base de connaissances pour une école en utilisant GNU Prolog. Cette base doit contenir les informations suivantes :
- Les élèves et leurs informations personnelles (nom, prénom, date de naissance, etc.).
- Les groupes de projet auxquels les élèves appartiennent.
- La gestion des notes des élèves dans différents modules.
- La liste des modules avec leur nom et description.

1. **Décrivez les faits et règles** nécessaires pour représenter ces informations dans votre programme Prolog.
2. **Écrivez un programme en Prolog** contenant des exemples de données et de règles. Par exemple, vous pourriez inclure :
   - Une règle pour trouver tous les élèves d’un groupe de projet spécifique.
   - Une règle pour calculer la moyenne des notes d’un élève dans un module.
   - Une règle pour lister les modules suivis par un élève.
3. **Montrez des exemples de requêtes** pour interroger la base de connaissances (par exemple, récupérer la liste des élèves dans un groupe, obtenir la moyenne des notes d'un élève).


## Exercice 2.2

Vous travaillez sur des exemples de classification avec des réseaux de neurones profonds utilisant TensorFlow. Les exemples actuels utilisent les jeux de données suivants :

 - [Traitement des données dans Tensorflow](../Projet/Data.ipynb)
 - [Reconnaissance de l'écriture manuscrite à l'aide des données du MNIST](../Projet/Introduction.ipynb)
 - [Classification des textes à l'aide des avis IMDB](../Projet/Textes.ipynb)
 
**Question :**
Vous allez travailler sur un exemple de classification de textes en utilisant le jeu de données **Reuters** disponible dans TensorFlow. Ce jeu de données contient des textes d’actualités classés dans différentes catégories, ce qui en fait un excellent jeu de données pour la classification de texte.

Votre tâche est d'explorer ce jeu de données et de développer un modèle de classification de texte en utilisant des réseaux de neurones profonds dans TensorFlow. Vous avez les objectifs suivants :

### Objectifs :

1. **Chargement et prétraitement des données** : 
   - Chargez le jeu de données **Reuters** à l’aide de `tf.keras.datasets.reuters`.
   - Prétraitez les données en veillant à convertir les textes en séquences de tokens numériques compatibles avec le modèle. Utilisez des techniques comme la tokenisation et le padding pour obtenir des séquences de longueur uniforme.
   - **Conseils** : Utilisez `Tokenizer` de `tf.keras.preprocessing.text` pour transformer les textes en séquences numériques et `pad_sequences` pour uniformiser la longueur des séquences.

2. **Construction d’un modèle de réseau de neurones** : 
   - Créez un modèle de réseau de neurones profond pour la classification des textes. Expérimentez avec différents types de couches pour trouver une architecture adaptée (par exemple, couches d'embedding pour les mots, couches denses, ou couches LSTM ou GRU pour capturer la structure des séquences).
   - **Conseils** : Essayez d’abord une architecture simple (comme une combinaison d’Embedding et Dense), puis explorez l’ajout de couches récurrentes pour une meilleure compréhension du contexte des mots.

3. **Optimisation des hyperparamètres** : 
   - Modifiez les hyperparamètres du modèle (par exemple, nombre de neurones, nombre de couches, taux d’apprentissage, nombre d’époques) et observez leur impact sur les performances du modèle.
   - **Conseils** : Commencez avec un taux d'apprentissage de base (par exemple, 0.001) et ajustez-le en fonction de la rapidité de convergence. Expérimentez également avec des tailles de batch différentes et observez leur effet.

4. **Entraînement et évaluation du modèle** :
   - Entraînez votre modèle en utilisant les données de Reuters et évaluez sa performance en termes de précision, rappel et score F1.
   - **Conseils** : Utilisez la fonction `classification_report` de `sklearn.metrics` pour obtenir un rapport de classification détaillé et `history` de Keras pour visualiser la précision et la perte au cours de l’entraînement.

5. **Analyse des résultats et visualisation** :
   - Comparez les différentes configurations testées en termes de performance. Incluez des graphiques pour illustrer la précision et la perte au fil des époques pour chaque configuration.
   - **Conseils** : Utilisez des graphiques pour représenter la précision d'entraînement et de validation au fil des époques, et comparez les modèles pour voir comment les choix d’architecture et d’hyperparamètres influencent les résultats.

6. **Documentation des observations et conclusions** :
   - Documentez les configurations testées (types de couches, hyperparamètres, etc.), les résultats obtenus et les observations sur les performances du modèle en fonction des ajustements effectués.


## Exercice 2.3

### Exercice 2.4 : Classification d'Images avec le Dataset CIFAR-10

Dans cet exercice, vous utiliserez le dataset **CIFAR-10** de TensorFlow pour construire et évaluer un modèle de réseau de neurones convolutif (CNN) capable de classifier des images en 10 catégories (avions, voitures, oiseaux, chats, etc.).

#### Objectifs

1. **Chargement et Prétraitement des Données** :
   - Chargez le dataset CIFAR-10 à partir de `tf.keras.datasets.cifar10`. Ce dataset contient 60 000 images de 32x32 pixels réparties en 10 classes, avec 50 000 images pour l'entraînement et 10 000 pour le test.
   - Normalisez les valeurs des pixels des images entre 0 et 1 pour faciliter l'apprentissage.
   - Appliquez des techniques d'augmentation de données (data augmentation) pour rendre le modèle plus robuste. Utilisez des transformations telles que la rotation, le zoom, et le retournement horizontal pour augmenter la diversité des images d'entraînement.

2. **Création d'un Modèle de Réseau de Neurones Convolutif (CNN)** :
   - Concevez un modèle CNN en utilisant des couches de convolution et de pooling pour extraire les caractéristiques importantes des images.
   - Structure suggérée :
     - **Couche de Convolution** : plusieurs filtres (par exemple, 32, 64, 128) avec une petite taille de filtre (3x3), suivis d'une activation ReLU.
     - **Couche de Pooling** : réduction de la taille des cartes de caractéristiques pour diminuer la complexité (par exemple, max pooling 2x2).
     - **Couches Denses** : après les couches convolutives, aplatissez les cartes de caractéristiques et ajoutez une ou plusieurs couches entièrement connectées pour la classification.
     - **Régularisation** : intégrez des techniques de régularisation comme le dropout ou la batch normalization pour éviter le surapprentissage.
   - Testez différentes architectures en ajoutant ou supprimant des couches pour observer leur impact sur les performances.

3. **Entraînement et Optimisation du Modèle** :
   - Entraînez le modèle en utilisant la fonction de perte `sparse_categorical_crossentropy`, car il s'agit d'un problème de classification multiclasses.
   - Utilisez l’optimiseur Adam et testez différents taux d'apprentissage pour voir leur effet sur la convergence (par exemple, commencez avec 0.001).
   - Ajustez d'autres hyperparamètres comme la taille de batch et le nombre d'époques, afin de trouver une configuration optimale qui équilibre précision et temps de calcul.

4. **Évaluation et Analyse des Performances** :
   - Évaluez le modèle sur l'ensemble de test et calculez la précision globale ainsi que la précision pour chaque classe.
   - Générez un rapport de classification (par exemple, avec `classification_report` de `sklearn.metrics`) et une matrice de confusion pour identifier les classes où le modèle est performant et celles où des améliorations sont possibles.

5. **Documentation et Visualisation des Résultats** :
   - Documentez les configurations testées (nombre de couches, hyperparamètres, etc.) et les performances obtenues.
   - Visualisez les courbes de précision et de perte d'entraînement et de validation au fil des époques pour analyser le comportement d'apprentissage du modèle.
   - Affichez des exemples de prédictions correctes et incorrectes afin de mieux comprendre les erreurs du modèle et d'identifier des pistes pour l’améliorer.

## Exercice 2.4
[Mini projet - comprendre la traduction des propriétés de Wikidata](../Projet/miniprojet-notebook.ipynb)


### Objectif de l'Exercice

Dans le cadre de votre mini-projet, vous allez tester des modèles d'apprentissage profond pour prédire les séquences de traductions possibles à partir des propriétés de Wikidata. 

#### Contexte

Considérez la séquence suivante saisie par l'utilisateur :

```
['it', 'fi']
```

Votre modèle doit être capable de renvoyer la langue suivante, par exemple :

```
['fr']
```

### Tâche

Votre objectif est de former un modèle de réseau neuronal capable de prédire la ou les prochaines traductions probables pour des étiquettes, descriptions ou alias. Pour cela, vous devez suivre les étapes ci-dessous :

1. **Préparation des Données**:
   - Utilisez la séquence de traduction des propriétés de Wikidata comme base de données.
   - Séparez les séquences en ensembles d'entraînement et de test.

2. **Modélisation**:
   - Implémentez un modèle de réseau neuronal.

3. **Évaluation**:
   - Après l'entraînement du modèle, évaluez ses performances sur l'ensemble de test.
   - Veuillez indiquer les mesures de précision et toute autre métrique pertinente pour évaluer la qualité des traductions prédites.

### Indications

- Pensez à prétraiter vos données, notamment en nettoyant les entrées et en les normalisant.
- Pour améliorer la performance de votre modèle, envisagez d'ajuster les hyperparamètres et de tester différentes architectures.

## Références
- [Multilayer Perceptron Explained with a Real-Life Example and Python Code: Sentiment Analysis](https://towardsdatascience.com/multilayer-perceptron-explained-with-a-real-life-example-and-python-code-sentiment-analysis-cb408ee93141)
- **Prévision des séries temporelles avec les modèles LSTM** : [Time Series Prediction with LSTM Recurrent Neural Networks in Python with Keras](https://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/)
