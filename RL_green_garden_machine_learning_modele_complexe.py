import numpy as np
from sklearn.linear_model import LinearRegression

# Données : [Budget_Pub, Température]
X_multi = np.array([
    [50, 15],
    [100, 20],
    [20, 25],
    [150, 18],
    [80, 22]
])

y_ca = np.array([1200, 2500, 1800, 3100, 2400])

# 1. Entraîner le modèle
modele_complexe = LinearRegression().fit(X_multi, y_ca) 

# 2. Définir le simulateur (prend 2 chiffres en entrée)
def simulateur_budget(budget_pub, temperature):  
    # On transforme les deux chiffres en le format attendu par l'IA
    entree_ia = np.array([[budget_pub, temperature]])
    
    # Prédiction
    pred = modele_complexe.predict(entree_ia) 
    return round(pred[0])  

# 3. Test du scénario [120€ de pub, 23°C]
resultat_ca = simulateur_budget(120, 23) 

print("-" * 40)
print(f"💰 Le CA prévu pour ce samedi est de : {resultat_ca}€")
print("-" * 40)