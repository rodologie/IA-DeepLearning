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

## Exercice 1.3 [★★★]
On vous a demandé de modéliser la base de connaissances d'une école concernant les élèves, leurs informations personnelles, 
leurs groupes de projet, la gestion de leurs notes et leurs différents modules. Ecrivez un programme GNU Prolog avec quelques 
exemples et montrez les différentes règles que vous allez alimenter dans votre base de connaissances.
