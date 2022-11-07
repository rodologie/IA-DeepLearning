# Travaux pratiques 1

**Année: 2022-2023**

## Objectifs

1.  Rappels sur numpy, scikit-learn etc.
2.	Implémentation de perceptron en Python
3.	Introduction à Tensorflow 2.0+

## Exercice 1.1 [★]
Votre premier exercice consiste à télécharger le [notebook Python Jupyter](TP1.ipynb) et à vous familiariser avec les différentes méthodes des bibliothèques: numpy, scikit-learn etc.

Téléchargez cette page web de Wikipedia : https://fr.wikipedia.org/wiki/Paris  et enregistrez le fichier en tant que HTML. Analysez et identifiez toutes les tâches possibles sur cette page. Écrivez un programme pour mettre en œuvre ces tâches. Les tâches possibles sont les suivantes :
- Extraction et analyse des mots (nombre d'occurrences), des liens (liens d'ancrage, interne et externe) et des images (taille).
- Extraction et identification des chiffres, des dates, des coordonnées géographiques, des noms propres (noms de personnes et de lieux).
- Identifier et extraire les données structurées, y compris les tableaux.
- Différencier les sections et les paragraphes


## Exercice 1.2 [★★]
En poursuivant l'analyse de la page Wikipédia téléchargée, écrivez un programme pour mettre en œuvre les tâches suivantes:
-	Appliquer les algorithmes de racination PorterStemmer et SnowballStemmer sur le texte de la page Wikipedia. Rappelez-vous que l'algorithme Porter Stemming a été créé pour la langue anglaise. Comparez les résultats des deux algorithmes, en particulier l'occurrence des racines les plus courantes et le nombre de racines uniques. 
-	Extrayez tous les 1-grammes (mots), 2-grammes (bi-grammes), 3-grammes, 4-grammes et 5-grammes du texte de Wikipedia et affichez les n occurrences les plus courantes de chacun. 
-  Étiquetage en parties du discours (PoS)
-  Lemmatisation
-  Analyse morphologique
-  Reconnaissance d'entités nommées
-  Word embeddings à l'aide de modèles Word2Vec (CPOW et Skip-gram)

Vous pouvez utiliser un ou plusieurs des packages suivants, dans la mesure du possible. Si
vous utilisez plus de deux packages, rédigez également un petit rapport sur la comparaison de vos résultats. 

1. nltk
2. spaCy
3. gensim

## Exercice 1.3 [★★]
Implémenter perceptron en Python avec les caractéristiques suivantes
1. Fonction d'activation configurable
2. Nombre d'entrées configurables 
3. Nombre d'époques et taux de formation configurables
4. Effectuer des prévisions

Tester votre modèle avec des fonctions simple.

## Exercice 1.4 [★★★]

Créer un modèle de réseau de neurones en utilisant Tensorflow. Votre objectif est de configurer les différents paramètres de votre modèle et tester le modèle avec l'ensemble de données d'écriture manuscrite du MNIST.
1. Le nombre de couches cachées
2. La configuration des couches cachées comme la fonction d'activation
3. Le taux d'abandon de votre modèle
4. Algorithmes d'optimisation
5. Fonctions de perte

Évaluez votre modèle en utilisant les différents indicateurs disponibles (précision etc.)

## Références
* [How To Implement The Perceptron Algorithm From Scratch In Python](https://machinelearningmastery.com/implement-perceptron-algorithm-scratch-python/)
