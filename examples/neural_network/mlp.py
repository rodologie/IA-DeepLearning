import numpy as np
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Fonction d'activation Sigmoïde
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Fonction d'activation ReLU
def relu(x):
    return np.maximum(0, x)

# Fonction de dérivée pour Sigmoïde et ReLU
def derivee_sigmoid(x):
    return x * (1 - x)

def derivee_relu(x):
    return np.where(x > 0, 1, 0)

# Propagation avant à travers le réseau
def propagation_avant(entree, poids, biais):
    activation = entree
    activations = [activation]  # stocke les activations de chaque couche pour le backprop

    # Propagation à travers chaque couche cachée
    for i in range(len(poids) - 1):
        z = np.dot(activation, poids[i]) + biais[i]
        activation = relu(z)  # on utilise ReLU pour les couches cachées
        activations.append(activation)
    
    # Couche de sortie (par ex., sigmoid pour une tâche de classification binaire)
    z = np.dot(activation, poids[-1]) + biais[-1]
    activation = sigmoid(z)
    activations.append(activation)

    return activations

# Fonction de perte (Binary Cross-Entropy)
def calcul_perte(y_pred, y_vrai):
    m = y_vrai.shape[0]
    perte = -np.sum(y_vrai * np.log(y_pred) + (1 - y_vrai) * np.log(1 - y_pred)) / m
    return perte



# Rétropropagation
def retropropagation(activations, poids, biais, y_vrai, taux_apprentissage=0.01):
    # Étape 1 : Calculer le gradient de la perte pour la couche de sortie
    erreur = activations[-1] - y_vrai
    deltas = [erreur * derivee_sigmoid(activations[-1])]

    # Étape 2 : Calculer les gradients pour chaque couche cachée
    for i in reversed(range(len(poids) - 1)):
        delta = np.dot(deltas[-1], poids[i + 1].T) * derivee_relu(activations[i + 1])
        deltas.append(delta)

    # Inverser les deltas pour qu'ils correspondent à chaque couche du réseau
    deltas = deltas[::-1]

    # Mise à jour des poids et biais
    for i in range(len(poids)):
        poids[i] -= taux_apprentissage * np.dot(activations[i].T, deltas[i])
        biais[i] -= taux_apprentissage * np.sum(deltas[i], axis=0, keepdims=True)

# Fonction d'entraînement
def entrainer_mlp(X, y, couches, epochs=1000, taux_apprentissage=0.01):
    # Initialisation des poids et biais
    poids = [np.random.rand(couches[i], couches[i + 1]) for i in range(len(couches) - 1)]
    biais = [np.random.rand(1, couches[i + 1]) for i in range(len(couches) - 1)]
    
    # Boucle d'entraînement
    for epoch in range(epochs):
        # Propagation avant
        activations = propagation_avant(X, poids, biais)
        
        # Calcul de la perte
        perte = calcul_perte(activations[-1], y)
        
        # Rétropropagation
        retropropagation(activations, poids, biais, y, taux_apprentissage)
        
        # Afficher la perte à intervalles réguliers
        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Perte: {perte:.4f}")
    
    return poids, biais

# Fonction de prédiction
def predire(X, poids, biais):
    activations = propagation_avant(X, poids, biais)
    return activations[-1]

# Étape 1 : Charger les données Iris
iris = load_iris()
X = iris.data  # caractéristiques
y = iris.target  # étiquettes

# Étape 2 : Prétraitement des données
# Normaliser les caractéristiques
X = (X - X.mean(axis=0)) / X.std(axis=0)

# One-hot encoding des étiquettes
encoder = OneHotEncoder(sparse_output=False)
y = encoder.fit_transform(y.reshape(-1, 1))

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Étape 3 : Entraîner le MLP
couches = [4, 5, 3]  # 4 neurones d'entrée, 5 neurones cachés, 3 neurones de sortie
poids, biais = entrainer_mlp(X_train, y_train, couches, epochs=1000, taux_apprentissage=0.01)

# Étape 4 : Faire des prédictions
y_pred = predire(X_test, poids, biais)

# Convertir les probabilités en classes prédites
y_pred_classes = np.argmax(y_pred, axis=1)

# Convertir les classes réelles pour évaluer les performances
y_test_classes = np.argmax(y_test, axis=1)

# Évaluer les résultats
accuracy = np.mean(y_pred_classes == y_test_classes)
print(f"Accuracy sur l'ensemble de test : {accuracy:.2f}")

