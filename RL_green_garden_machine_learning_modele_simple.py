import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Préparer les données
X_prix = np.array([10, 15, 20, 25, 30]).reshape(-1,1)
y_quantite = np.array([50, 40, 30, 22, 10])

# 2. Créer et entraîner le modèle
modele_simple = LinearRegression()
modele_simple.fit(X_prix, y_quantite)

# 3. Prédire pour 22€
prix_test = [[22]]
prediction = modele_simple.predict(prix_test)
print(f"Pour 22€, on prévoit d'en vendre : {prediction[0]}")