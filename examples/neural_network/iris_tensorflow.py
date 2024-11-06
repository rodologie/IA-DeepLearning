import numpy as np
import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# 1. Préparation des données
# Charger le jeu de données IRIS
data = load_iris()
X = data.data  # Les caractéristiques
y = data.target.reshape(-1, 1)  # Les étiquettes

# Encodage en one-hot des étiquettes
encoder = OneHotEncoder(sparse_output=False)
y_encoded = encoder.fit_transform(y)

# Division en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Normalisation des données
mean = X_train.mean(axis=0)
std = X_train.std(axis=0)
X_train = (X_train - mean) / std
X_test = (X_test - mean) / std

# 2. Création du modèle
model = Sequential([
    Dense(10, activation='relu', input_shape=(X.shape[1],)),
    Dense(10, activation='relu'),
    Dense(3, activation='softmax')
])

# Compilation du modèle
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 3. Définition des callbacks
# Arrêt anticipé pour éviter le surapprentissage
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Sauvegarde du meilleur modèle
checkpoint = ModelCheckpoint('best_model.keras', monitor='val_loss', save_best_only=True)

# 4. Entraînement du modèle
history = model.fit(X_train, y_train,
                    validation_split=0.2,
                    epochs=100,
                    batch_size=4,
                    callbacks=[early_stopping, checkpoint])

# 5. Évaluation du modèle
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")

# 6. Visualisation des performances
# Visualisation de la courbe de perte et de précision
plt.figure(figsize=(12, 5))

# Courbe de perte
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Courbe de perte')
plt.legend()

# Courbe de précision
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Courbe de précision')
plt.legend()

plt.show()

# 7. Chargement du meilleur modèle sauvegardé et prédiction
best_model = tf.keras.models.load_model('best_model.keras')

# Prédiction sur les données de test
y_pred = best_model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true_classes = np.argmax(y_test, axis=1)

# Affichage de quelques prédictions pour vérifier le modèle
print("Vraies classes:", y_true_classes)
print("Classes prédites:", y_pred_classes)

