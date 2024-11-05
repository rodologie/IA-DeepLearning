import numpy as np

class Perceptron:
    def __init__(self, taux_apprentissage=0.01, n_iterations=1000):
        self.taux_apprentissage = taux_apprentissage
        self.n_iterations = n_iterations
        self.poids = None
        self.biais = None

    def ajuster(self, X, y):
        n_exemples, n_caracteristiques = X.shape
        self.poids = np.zeros(n_caracteristiques)
        self.biais = 0

        for _ in range(self.n_iterations):
            for i in range(n_exemples):
                ligne = X[i]
                y_calculé = np.dot(ligne, self.poids) + self.biais
                prediction = 1 if y_calculé >= 0 else 0
                erreur = y[i] - prediction
                # Mise à jour des poids et biais
                self.poids += self.taux_apprentissage * erreur * ligne
                self.biais += self.taux_apprentissage * erreur

    def predire(self, X):
        y_calculé = np.dot(X, self.poids) + self.biais
        return np.where(y_calculé >= 0, 1, 0)

# Données d'exemple
X = np.array([[1, 1], [2, 2], [1.5, 1.5], [0, 0], [0.5, 0.5], [1, 0]])
y = np.array([1, 1, 1, 0, 0, 0])

# Création et entraînement du perceptron
perceptron = Perceptron(taux_apprentissage=0.1, n_iterations=10)
perceptron.ajuster(X, y)

# Prédiction
print(perceptron.predire(np.array([[1, 1], [0, 0]])))  # Sortie : [1 0]

