# Calcul de la marge commerciale

prix_achat = float(input("Saisir le prix d'achat HT : "))
prix_vente = float(input("Saisir le prix de vente HT : "))

marge = prix_vente - prix_achat

if prix_achat <= 0 or prix_vente < 0:
    print("Erreur : les prix doivent être valides.")
else:
    taux_marge = (marge / prix_achat) * 100
    taux_marque = (marge / prix_vente) * 100 if prix_vente != 0 else 0

    print(f"Marge commerciale : {marge:.2f} DT")
    print(f"Taux de marge : {taux_marge:.2f} %")
    print(f"Taux de marque : {taux_marque:.2f} %")
