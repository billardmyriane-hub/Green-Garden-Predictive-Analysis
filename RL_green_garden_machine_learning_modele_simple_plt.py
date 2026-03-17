import matplotlib.pyplot as plt 

# 2. On trace la courbe historique
plt.figure(figsize=(10, 5)) 
plt.plot(X_prix, y_quantite,  
         marker='o',          
         linestyle='-',        
         color='tab:red',      
         linewidth=2,
         label='Données réelles') 


# On ajoute le point prédit pour 22€ (environ 26 unités)
plt.scatter(22, 26, color='green', s=100, zorder=5, label='Prédiction (22€)')
# -----------------------------------

# 3. Personnalisation 
plt.title('Analyse de l\'Élasticité Prix - Green Garden', fontsize=14) 
plt.xlabel('Prix Unitaire (€)') 
plt.ylabel('Quantité vendue (unités)') 
plt.legend() # Pour afficher les labels 'Données réelles' et 'Prédiction'
plt.grid(True, linestyle='--', alpha=0.6) 

plt.show()