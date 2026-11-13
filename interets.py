# Calcul des intérêts simples

capital = float(input("Saisir le capital (DT) : "))
taux = float(input("Saisir le taux annuel (en %) : "))
duree = float(input("Saisir la durée (en années) : "))

if capital < 0 or taux < 0 or duree < 0:
    print("Erreur : les valeurs doivent être positives.")
else:
    interets = capital * taux * duree / 100
    montant_final = capital + interets

    print(f"Intérêts simples : {interets:.2f} DT")
    print(f"Montant final : {montant_final:.2f} DT")
