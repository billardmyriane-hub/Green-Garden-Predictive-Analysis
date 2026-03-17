# On génère les prédictions pour nos données d'entraînement
y_pred_total = modele_complexe.predict(X_multi)

plt.figure(figsize=(10, 5))
plt.plot(y_ca, 'o-', label='CA Réel', color='tab:blue')
plt.plot(y_pred_total, 's--', label='CA prédit', color='tab:orange')

plt.title('Performance du Modèle Complexe (Pub + Météo)')
plt.ylabel('Chiffre d\'Affaires (€)')
plt.xlabel('Échantillons (Samedis passés)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()