# Calcul du montant de la TVA

montant_ht = float(input("Saisir le montant HT : "))
taux_tva = float(input("Saisir le taux de TVA (7 ou 13) : "))

if montant_ht < 0 or taux_tva < 0:
    print("Erreur : les valeurs doivent être positives.")
else:
    montant_tva = montant_ht * taux_tva / 100
    montant_ttc = montant_ht + montant_tva

    print(f"Montant de la TVA : {montant_tva:.2f} DT")
    print(f"Montant TTC : {montant_ttc:.2f} DT")
